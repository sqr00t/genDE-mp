import os, pymysql
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

class DB:
    """Abstracted pymysql functions to call as context managers"""
    def __init__(self, table: str, action: str):
        load_dotenv()
        #_env_vars = {i:os.environ.get(i) for i in ["mysql_host", "mysql_user", "mysql_pass", "mysql_db"]}
        #self.conn = pymysql.connect(**_env_vars)
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")
        self.conn = pymysql.connect(
                        host=host,
                        user=user,
                        password=password,
                        database=database
                    )
        self.cursor = None
        self.action = action
        self.table = table
        
    def __enter__(self): return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): self.close()
    
    def close(self):
        self.conn.close()
    
    def handler(self, data_var=None): #accepts optional single dictionary as argument
        """Handles action according to init->action:str. data is a dictionary passed when calling handler()"""
        actions = {
            "r": self.get_data,
            "a": self.insert_data,
            "d": self.delete_data,
            "u": self.update_data
        }
        if data_var: self.data = data_var
        else: self.data = None
        
        try:
            if self.action in actions.keys():
                task = actions.get(self.action)
            return task()
        except Exception as e: return print(f"Action failed. {e}")
        finally: self.cursor.close()
    
    def checker(self): #compare keys of inserted data dictionary vs. keys of table
        self.cursor = self.conn.cursor()
        self.cursor.execute(f'SELECT * FROM {self.table}')
        column_names = [i[0] for i in self.cursor.description]
        datakeys = self.data.keys()
        if bool(datakeys == column_names): return True
        else: return "No matching entry found on server."
    
    #SQL: if self.dictslist is None([]), select self.filename table and get table object, append to self.dictslist, enumerate self.dictslist, else enumerate self.dictslist
    def get_data(self):
        self.cursor = self.conn.cursor(DictCursor)
        self.cursor.execute(f'SELECT * FROM {self.table}')
        data = self.cursor.fetchall()
        return data #returns iterable obj (list of dictionaries)

    #SQL: try-catch incomplete fields, return new_dict() with error message if empty, else INSERT
    def insert_data(self):
        match_res = self.checker()
        if match_res:
            try:
                columns = ', '.join(self.data.keys())
                n_placeholders = ', '.join(['%s'] * len(self.data.keys()))
                sql = f"INSERT INTO {self.table} ({columns}) VALUES ({n_placeholders})"
                values_placeholder = tuple(self.data.values())
                self.cursor.execute(sql, values_placeholder)
                self.conn.commit()
                return f"Successfully inserted into {self.table} table"
            except Exception as e:
                self.conn.rollback()
                raise e
        else: return match_res

    #SQL: select from table vars matching values of oldDict, update with last updated self.dictslist[indexToUpdate]
    def update_data(self):
        match_res = self.checker()
        if match_res:
            try:
                columns = ', '.join([f'{k}=%s' for k in list(self.data.keys())[1:]])
                sql = f"UPDATE {self.table} SET {columns} WHERE id={self.data['id']}"
                self.cursor.execute(sql, tuple(self.data.values())[1:])
                self.conn.commit()
                return f"Successfully updated {self.table} table"
            except Exception as e:
                self.conn.rollback()
                raise e
        else: match_res

    #SQL: try: delete from table entry matching dictslist[indexdel] field values, return below
    # except SQL cannot find matching entry or .index out of scope., return Error no entry matching index
    def delete_data(self):
        match_res = self.checker()
        if match_res:
            try:
                sql = f"DELETE FROM {self.table} WHERE id={self.data['id']}"
                self.cursor.execute(sql)
                self.conn.commit()
                return f"Successfully deleted from {self.table} table"
            except Exception as e:
                self.conn.rollback()
                raise e
        else: return match_res

class CRUD:
    """Uses DB class to make CRUD relevant context manager functions for single line calling in MPFunctions"""
    def __init__(self, listname):
        self.listname = listname

    def create(self, data):
        """Inserts data to self.listname"""
        with DB(self.listname, "a") as db:
            return db.handler(data)
    
    def read(self):
        """Reads data from server, returns list of dictionaries"""
        with DB(self.listname, "r") as db:
            res = db.handler()
            print(f"Fetched {self.listname} data from server!")
        return res #loop this return val for printout

    def update(self, data):
        """Updates dict data from operation into matching id in self.listname table"""
        with DB(self.listname, "u") as db:
            return db.handler(data)

    def delete(self, data):
        """Deletes from self.listname table with id value of matching data from self.dictlist"""
        with DB(self.listname, "d") as db:
            return db.handler(data)
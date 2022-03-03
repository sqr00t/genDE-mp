import os.path, sys
sys.path.append(os.path.abspath('..'))

#import unittest
#from unittest.mock import patch, Mock
from core.DBfunctions import CRUD

def test_create_person():
    #expects last entry from read data == entered data
    expected = {
        'first_name': 'Solomon',
        'last_name': 'Yu',
        'age': 22,
        'email': "solomon.sj.yu"
        }
    
    #insert expected to DB
    CRUD("person").create(expected)
    
    read_from_server = CRUD("person").read()[-1]
    
    #ammend id to expected
    expected['person_id'] = read_from_server['person_id']
    
    results = read_from_server
    assert results == expected
    
def test_update_person():
    expected = {
        'person_id': 31,
        'first_name': 'Solomon Sui Jing',
        'last_name': 'Yu',
        'age': 26,
        'email': "solomon.sj.yu"
        }
    
    #update DB at p_id = 31
    CRUD("person").update(expected)
    
    read_from_server = CRUD("person").read()
    
    #result
    for dicts in read_from_server:
        if dicts['person_id'] == 31:
            result = dicts
            
    assert result == expected

def test_read_person():
    """Gets first dict entry of dictslist read from server, compares with expected dict k:vs"""
    expected = {
        'person_id':1,
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'email': None
        }

    read_from_server = CRUD("person").read()[0]

    results = read_from_server
    assert results == expected

def test_delete_person(): pass
#   data = {
#           'person_id': 1
#       }
#   try:
#       CRUD("person").delete(data)
#   except Exception as e:
#       print(f"Error: {e}")

def test_DB_private_connection(): pass
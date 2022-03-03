import os.path, sys
sys.path.append(os.path.abspath('..'))

#import unittest
#from unittest.mock import patch, Mock
from core.MPFunctions import Products, Couriers, Orders

class TestProducts:
    def __init__(self):
        self.test_dict = {'a':1, 'b':2, 'c':3, 'd':4}
        self.test_dictslist = [{'e':5, 'f':6, 'g':7, 'h':8}, {'i':9, 'j':10, 'k':11, 'l':12}]
    
    def test_new_products_dict(self): pass
    
    def test_insert_new_dict_to_dictslist(self): pass
    
    def test_update_dict_in_dictslist(self): pass
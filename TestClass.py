# -*- coding: utf-8 -*-

## Use: py.test -s TestClass.py

from math import log10

def setup_module(module):
    print ("Module:%s" % module.__name__)
 
def teardown_module(module):
    print ("Module: %s" % module.__name__)
 
def setup_function(function):
    print ("Function: %s" % function.__name__)
 
def teardown_function(function):
    print ("Function: %s" % function.__name__)

def test_strings():
	a = "efsdkfjhsdklyhfsdafdsloijhoityu"
	b = "efsdkfjhsdklyhfsdafdsloijhoityu"

	assert a == b

class TestClass:
 
    def setup_class(cls):
        print ("Class:%s" % cls.__name__)
 
    def teardown_class(cls):
        print ("Class: %s" % cls.__name__)
 
	def setup_method(self, method):
		print ("Method: %s" % method.__name__)

	def teardown_method(self, method):
		print ("Method: %s" % method.__name__)
 
    def test_log10(self):
    	print "======== LOG 10 ======"
        assert log10(10) == 1
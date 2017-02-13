'''this file is to test all functions in the main core file'''
import core
import os

def create_test_file(filename):
    '''creates a file to be tested for the functions'''
    with open(filename, 'w') as file:
        file.write('')


def test_total():
    '''this test testes the function total'''
    j = core.total('filename', 'test', 'February 03, 2017', 'Test', 2.00, 5.00)
    assert j == 'February 03, 2017 test Test 2.5\n'


def test_inventory():
    '''testes the function inventory'''
    create_test_file('test.txt')
    with open('test.txt', 'a') as file:
        file.write('test, Test, TeSt\n')
        file.write('test, Test, TeSt')
    k = core.inventory('test.txt')
    assert k == 'test, Test, TeSt\n'
    os.remove('test.txt')

def test_add_inv():
    '''test the function add_inv '''
    create_test_file('test.txt')
    with open('test.txt', 'a') as file:
        file.write('test, Test, TeSt\n')
    vari = core.add_inv('test.txt', 'batman', 'dvd')
    assert vari == 'batman, dvd, 5.0, 20.0\n'
    os.remove('test.txt')

'''this file is to test all functions in the main core file'''
import core

def test_total():
    '''this test testes the function total'''
    j = core.total('filename', 'test', 'February 03, 2017', 'Test', 2.00, 5.00)
    assert j == 'February 03, 2017 test Test 2.5'

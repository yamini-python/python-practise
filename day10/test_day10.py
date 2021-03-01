import pytest
from day10 import app

def test_user_get_200():
    test = app.test_client()
    response = test.get('/user')
    status=response.status_code
    assert status == 200

def test_user_post_200():
    test = app.test_client()
    response = test.post('/user',json={"name":"abcdijk","password":"xzzdzf"})
    status=response.status_code
    assert status == 200  

def test_user_username_get_200():
    test = app.test_client()
    response = test.get('/user/abcdi')
    status=response.status_code
    assert status == 200  

def test_user_username_post_200():
    test = app.test_client()
    response = test.put('/user/abcdd',json={"password":"xzzdzfi"})
    status=response.status_code
    assert status == 200

def test_user_username_delete_200():
    test = app.test_client()
    response = test.delete('/user/abcdi')
    status=response.status_code
    assert status == 200   

def test_create_get_400():
    test = app.test_client()
    response = test.get('/user/yaminis')
    status=response.status_code
    assert status == 400   

def test_create_delete_400():
    test = app.test_client()
    response = test.delete('/user/yaminis')
    status=response.status_code
    assert status == 400   

def test_create_put_400():
    test = app.test_client()
    response = test.put('/user/yaminis')
    status=response.status_code
    assert status == 400  

def test_validate_400():
    test = app.test_client()
    response = test.post('/user',json={"name":"a","password":"x"})
    status=response.status_code
    assert status == 400

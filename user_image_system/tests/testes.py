from urllib.error import URLError
import requests
import unittest
import json

URL = "http://127.0.0.1:9000"
ENDPOINT = "/user/filter"


def get_list_of_users_with_filter(initial_id: int, final_id: int):
    url = URL + ENDPOINT + "/" + str(initial_id) + "/" + str(final_id)
    response = requests.get(url)

    return response


def successful_tests(initial_id: int, final_id: int):
    response = get_list_of_users_with_filter(initial_id, final_id)
    list_users = json.loads(response.text)
    assert response.text == """[{"name":"Caio","user_id":1},{"name":"Pedro","user_id":2},{"name":"Augusto","user_id":3},{"name":"Fernando","user_id":4},{"name":"Joao","user_id":5}]"""
    assert response.status_code == 200
    assert list_users[0]["user_id"] == 1
    assert list_users[4]["user_id"] == 5


def error_tests(initial_id: int, final_id: int):
    response = get_list_of_users_with_filter(initial_id, final_id)
    assert response.text == """{"detail":"List of Users between 'id_initial=5' and 'id_final=1' not found."}"""
    assert response.status_code == 404

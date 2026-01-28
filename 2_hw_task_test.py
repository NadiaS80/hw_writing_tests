import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
url = 'https://cloud-api.yandex.net/v1/disk/resources'


@pytest.fixture
def creating_folder_on_yandex_disk_and_then_remove_it():
    """
    Create a folder on Yandex.Disk, return HTTP responses for create/check, and delete the folder after the test.
    """
    params = {'path': 'test_folder'}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    create_responce = requests.put(url, params=params, headers=headers)
    response = requests.get(url, params=params, headers=headers)
    yield (create_responce, response)
    requests.delete(url, params=params, headers=headers)


@pytest.fixture
def creating_folder_on_yandex_disk_with_untoken():
    """
    Attempt to create a folder on Yandex.Disk using an invalid token and return the HTTP response.
    """
    unTOKEN = '111'
    params = {'path': 'test_folder'}
    headers = {'Authorization': f'OAuth {unTOKEN}'}
    response = requests.put(url, params=params, headers=headers)
    return response


@pytest.fixture
def creating_double_folder_on_yandex_disk_and_then_remove_it():
    """
    Create a folder once and attempt to create it again to trigger a conflict; delete the folder after the test.
    """
    params = {'path': 'test_double_folder'}
    headers = {'Authorization': f'OAuth {TOKEN}'}
    requests.put(url, params=params, headers=headers)
    response = requests.put(url, params=params, headers=headers)
    yield response
    requests.delete(url, params=params, headers=headers)


def test_create_folder_success(creating_folder_on_yandex_disk_and_then_remove_it):
    """
    Verify that folder creation succeeds and the created folder can be fetched from the API.
    """
    assert creating_folder_on_yandex_disk_and_then_remove_it[0].status_code == 201
    assert creating_folder_on_yandex_disk_and_then_remove_it[1].status_code == 200


def test_create_folder_with_untoken(creating_folder_on_yandex_disk_with_untoken):
    """
    Verify that creating a folder with an invalid token returns an authorization error.
    """
    assert creating_folder_on_yandex_disk_with_untoken.status_code == 401


def test_create_double_folder(creating_double_folder_on_yandex_disk_and_then_remove_it):
    """
    Verify that creating the same folder twice returns a conflict error.
    """
    assert creating_double_folder_on_yandex_disk_and_then_remove_it.status_code == 409
import random
from json import dumps, loads
from uuid import uuid4

import pytest
import requests
from assertpy.assertpy import assert_that
from jsonpath_ng import parse

from config import BASE_URI
from utils.file_reader import read_file
# from utils.print_helpers import pretty_print

from assertpy.assertpy import soft_assertions


def test_read_all_has_easter():
    # We use the requests.get() with rrl to make a get request
    response = requests.get(BASE_URI)
    # response from requests has many useful properties
    # we can assert on the response status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    # We can get python dict as response by using .json() method
    peoples = response.json()
    # pretty_print(peoples)
    first_names = [people['fname'] for people in peoples]
    assert_that(first_names).contains('Easter')
    # assert_that(response_content).extracting('fname').is_not_empty().contains('Jack')


def test_read_all_has_jack():
    response = requests.get(BASE_URI)
    with soft_assertions():
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        response_text = response.json()
        assert_that(response_text).extracting('fname').is_not_empty().contains('Jack')
        # assert_that(response_text).extracting('fname').is_not_empty().contains('Beck')


def test_new_person_can_be_added():
    unique_last_name = create_new_person()

    # After user is created, we read all the users and then use filter expression to find if the
    # created user is present in the response list
    peoples = requests.get(BASE_URI).json()
    # is_new_user_created = search_created_user_in(peoples, unique_last_name)
    # is_new_user_created = filter(lambda person: person['lname'] == unique_last_name, peoples)
    # assert_that(is_new_user_created).is_not_empty()
    new_users = [person for person in peoples if person['lname'] == unique_last_name]
    assert_that(new_users).is_not_empty()


def test_new_person_can_be_added_with_if_statement_method():
    unique_last_name = create_person_with_unique_last_name()

    # After user is created, we read all the users and then use filter expression to find if the
    # created user is present in the response list
    peoples = requests.get(BASE_URI).json()
    is_new_user_created = search_created_user_in(peoples, unique_last_name)
    # is_new_user_created = filter(lambda person: person['lname'] == unique_last_name, peoples)
    assert_that(is_new_user_created).is_not_empty()
    # new_users = [person for person in peoples if person['lname'] == unique_last_name]
    # assert_that(new_users).is_not_empty()


def test_created_person_can_be_deleted_by_id():
    persons_last_name = create_new_person()

    peoples = requests.get(BASE_URI).json()
    newly_created_user = search_created_user_in(peoples, persons_last_name)[0]

    print(newly_created_user)
    person_to_be_deleted = newly_created_user['id']

    delete_url = f'{BASE_URI}/{person_to_be_deleted}'
    response = requests.delete(delete_url)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_created_person_can_be_deleted_by_lname():
    persons_last_name = create_new_person()

    peoples = requests.get(BASE_URI).json()
    newly_created_user = search_created_user_in(peoples, persons_last_name)[0]

    print(newly_created_user)
    person_to_be_deleted = newly_created_user['lname']

    delete_url = f'{BASE_URI}/{person_to_be_deleted}'
    response = requests.delete(delete_url)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


@pytest.fixture
def create_data():
    payload = read_file('create_person.json')

    random_no = random.randint(0, 1000)
    last_name = f'Olabini{random_no}'

    payload['lname'] = last_name
    yield payload


def test_person_can_be_added_with_a_json_template(create_data):
    create_person_with_unique_last_name(create_data)

    response = requests.get(BASE_URI)
    peoples = loads(response.text)

    # Get all last names for any object in the root array
    # Here $ = root, [*] represents any element in the array
    # Read full syntax: https://pypi.org/project/jsonpath-ng/
    jsonpath_expr = parse("$.[*].lname")
    result = [match.value for match in jsonpath_expr.find(peoples)]

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)


def create_person_with_unique_last_name(body=None):
    if body is None:
        # Ensure a user with a unique last name is created everytime the test runs
        # Note: json.dumps() is used to convert python dict to json string
        last_name = f'User{str(uuid4())}'
        unique_last_name = last_name[:32]
        # unique_last_name = 'Winter'
        payload = dumps({
            'fname': 'Jack',
            'lname': unique_last_name
        })
    else:
        unique_last_name = body['lname']
        payload = dumps(body)

    # Setting default headers to show that the client accept json
    # And will send json in the header
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # We use requests.post method with keyword params to make the request more readable
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(201)
    # assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)
    return unique_last_name


def create_new_person():
    # Ensure a user with a unique last name is created everytime the test runs
    # Note: json.dumps() is used to convert python dict to json string
    last_name = f'User{str(uuid4())}'
    unique_last_name = last_name[:32]
    # unique_last_name = 'Winter'
    payload = dumps({
        'fname': 'Jack',
        'lname': unique_last_name
    })

    # Setting default headers to show that the client accept json
    # And will send json in the header
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # We use requests.post method with keyword params to make the request more readable
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(201)
    # assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)
    return unique_last_name


def search_created_user_in(peoples, last_name):
    return [person for person in peoples if person['lname'] == last_name]

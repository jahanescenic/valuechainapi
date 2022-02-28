import requests
import json
import jsonpath
import random
import string
import os

baseUrl = "http://restapi.adequateshop.com/"


def random_user(c_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(c_num))


def random_password():
    n = 10
    return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])


def create_test_data_directory_if_not_exist():

    path = './TestData'

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)


def create_user_json():
    # Create TestData folder if not exist
    create_test_data_directory_if_not_exist()

    # Create Random user data
    name = random_user(7)
    email = name+"@gmail.com"
    password = random_password()
    data = {"name": name, "email": email, "password": password}
    with open('TestData/sample-user.json', 'w') as outfile:
        json.dump(data, outfile)


def test_user_registration():
    create_user_json()

    # Retrieve random user data (name, email, password)
    file = open('TestData/sample-user.json', "r")
    inputData = json.loads(file.read())

    # Send POST Request
    path = "api/authaccount/registration"
    response = requests.post(url=baseUrl+path, json=inputData)
    responseJson = json.loads(response.text)

    # Print new user data in Test report
    print(responseJson)

    # Store user registration response for further test
    with open('TestData/successful_user_registration.json', "w") as outfile:
        json.dump(responseJson, outfile)

    # Assertion Starts with Status 200
    assert response.status_code == 200, "Status should be 200"
    assert jsonpath.jsonpath(responseJson, '$.data.Name')[
        0] == inputData['name'], "Username should be " + inputData['name']

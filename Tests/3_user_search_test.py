import requests
import json
import jsonpath

baseUrl = "http://restapi.adequateshop.com/"


def test_user_search():
    path = "api/users/"

    # Retrieve Id and Token from user login session
    file = open('TestData/successful_user_registration.json', "r")
    fileData = json.loads(file.read())
    id = fileData["data"]["Id"]
    token = fileData["data"]["Token"]

    # Send GET Request with login token
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(url=baseUrl+path+str(id), headers=headers)
    responseJson = json.loads(response.text)

    # Print new user data in Test report
    print(responseJson)

    # Assertion Starts with status 200
    assert response.status_code == 200, "Status should be 200"

    # Validate id, name and email are matching with the successful user registration  response 
    assert jsonpath.jsonpath(responseJson, '$.id')[
        0] == fileData["data"]["Id"], \
        "ID didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.name')[
        0] == fileData["data"]["Name"], \
        "Name didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.email')[
        0] == fileData["data"]["Email"], \
        "Email didn't Match with user registration Data"

import requests
import json
import jsonpath

baseUrl = "http://restapi.adequateshop.com/"


def test_user_login():
    # Retrieve Email and Password from sample data
    file = open('TestData/sample-user.json', "r")
    fileData = json.loads(file.read())
    email = fileData["email"]
    password = fileData["password"]

    # Construct Input Data and Send POST Request
    inputData = {"email": email, "password": password}
    path = "api/authaccount/login"
    response = requests.post(url=baseUrl+path, json=inputData)
    responseJson = json.loads(response.text)

    # Print new user data in Test report
    print(responseJson)

    # Writing Last Updated User Token
    with open('TestData/successful_user_registration.json', "w") as outfile:
        json.dump(responseJson, outfile)

    # Assertion Starts with Status 200
    assert response.status_code == 200, "Status should be 200"

    # Verify Id, Name, Email of the user retrieved
    file = open('TestData/successful_user_registration.json', "r")
    fileData = json.loads(file.read())

    # Validate id, name and email are matched with successful registration response
    assert jsonpath.jsonpath(responseJson, '$.data.Id')[
        0] == fileData["data"]["Id"], \
        "ID didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.data.Name')[
        0] == fileData["data"]["Name"], \
        "Name didn't Match with user registration Data"
    assert jsonpath.jsonpath(responseJson, '$.data.Email')[
        0] == fileData["data"]["Email"], \
        "Email didn't Match with user registration Data"

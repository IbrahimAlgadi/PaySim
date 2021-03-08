from fastapi.testclient import TestClient

from smart_node import app

client = TestClient(app)


def test_smart_node_successful_payment():
    # create a request
    params = {
        'user': "username",
        'token': "token provided by Smart Node Company",
        'card': "2222222222222222",
        'amount': 500,
        'expDate': '22/12',
        'pin': "1212"
    }
    # Send request to smart node payment end point
    response = client.post("/payment", json=params)
    # print(response.json())
    # the response should be successful
    assert response.status_code == 200
    # successful payment
    assert response.json()['status'] == True


def test_smart_node_failed_payment():
    # create a request
    params = {
        'user': "username",
        'token': "token provided by Smart Node Company",
        'card': "4444444444444444",
        'amount': 500,
        'expDate': '22/12',
        'pin': "1212"
    }
    # Send request to smart node payment end point
    response = client.post("/payment", json=params)
    # print(response.json())
    assert response.status_code == 200
    # the error payment
    assert response.json()['status'] == False

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_syberpay_get_url_returns_url_function():
    # create a request
    params = {
        'applicationId': "applicationId",
        'payeeId': "PayeeId",
        'serviceId': "serviceId",
        'customerRef': "customerRef",
        'amount': 2000,
        'currency': 'SDG',
        'hash': "request hash"
    }
    # send port request to the payment url of cyberpay test client
    response = client.post("/syberpay/getUrl", json=params)
    # the response should be successful
    assert response.status_code == 200
    # the amount is correct
    assert response.json()['amount'] == params['amount']
    # there is a payment url generated
    assert type(response.json()['paymentUrl']) == str
    assert len(response.json()['paymentUrl']) > 0

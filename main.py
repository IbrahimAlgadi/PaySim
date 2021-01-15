from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import *
import datetime
import uuid
import requests
from requests.exceptions import RequestException as ReqConErr
from faker import Faker
from decouple import config

BASE_URL = f"http://{config('S_HOST', default='127.0.0.1')}:{config('S_PORT', default=5000, cast=int)}"

# import requests

fake = Faker()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

storage = {}


@app.post("/syberpay/getUrl")
async def get_url(paymentRequest: PaymentRequest):
    transaction_id = uuid.uuid4()
    initial_payment = InitiatePayment(**{

        "applicationId": paymentRequest.applicationId,
        "payeeId": paymentRequest.payeeId,
        "serviceId": paymentRequest.serviceId,
        "amount": paymentRequest.amount,
        "currency": paymentRequest.currency,
        "customerRef": paymentRequest.customerRef,
        "tranTimestamp": f"{datetime.datetime.now()}",
        "paymentInfo":
            {
                "accountNo": "123456",
                "customerName": fake.name(),
                "serviceType": "123",
            },
        "responseCode": 1,
        "responseMessage": "Approved",
        "paymentUrl": f"{BASE_URL}/syberpay/payment/{transaction_id}"

    })
    storage[f"{transaction_id}"] = {"payment": initial_payment, "payment_status": False}
    # print(storage)
    return initial_payment


@app.post("/syberpay/payment_status")
async def payment_status(paymentReq: PaymentStatusReq):
    # print(paymentReq)
    transaction_id = paymentReq.transactionId
    initial_payment = storage[transaction_id]['payment']
    # print(storage[transaction_id])
    if storage[transaction_id]["payment_status"]:
        return PaymentStatusResp(**{
            "status": "Successful",
            "responseCode": 1,  # anything else the thing has fallen so say transaction didn't go through
            "responseMessage": "Approved",
            "payment": {
                "applicationId": paymentReq.applicationId,
                "payeeId": "0010010009",
                "serviceId": "001001000901",
                "amount": initial_payment.amount,
                "currency": initial_payment.currency,
                "customerRef": initial_payment.customerRef,
                "tranTimestamp": initial_payment.tranTimestamp,
                "paymentInfo": initial_payment.paymentInfo,
                "responseData": {
                    "receiptNo": "972XY30"
                },
                "responseCode": 0,
                "responseMessage": "Approved",
                "status": "Successful"
            }
        })
    else:
        return PaymentStatusResp(**{
            "status": "Pending",
            "responseCode": 2,  # anything else the thing has fallen so say transaction didn't go through
            "responseMessage": "Invalid Transaction Amount/Currency",
            "payment": {
                "applicationId": paymentReq.applicationId,
                "payeeId": "0010010009",
                "serviceId": "001001000901",
                "amount": initial_payment.amount,
                "currency": initial_payment.currency,
                "customerRef": initial_payment.customerRef,
                "tranTimestamp": initial_payment.tranTimestamp,
                "paymentInfo": initial_payment.paymentInfo,
                "responseData": {
                    "receiptNo": "972XY30"
                },
                "responseCode": 2,
                "responseMessage": "Invalid Transaction Amount/Currency",
                "status": "Failure"
            }
        })


# when customer pay call my server hook
@app.get('/syberpay/payment/{transactionId}')
async def cusomer_pay(request: Request, transactionId: str):
    return templates.TemplateResponse("syber_form.html", {"request": request, "transactionId": transactionId})


@app.post('/syberpay/payment/{transactionId}')
async def cusomer_pay(request: Request, transactionId: str):
    storage[f"{transactionId}"]["payment_status"] = True
    print(storage)
    try:
        rq = requests.post('localhost:8000/syber/hook/event/', json={
            'transactionId': transactionId
        })
    except ReqConErr:
        return {'transactionId': transactionId}
    # print("Customer Paid successfully ... done some action, this hook that tell you what has happened in syberpay")
    return {'transactionId': transactionId}


# when customer pay call my server hook
@app.post('/simulate/call/other/website/hook/')
async def cusomer_done_payment():
    print("Customer Paid successfully ... done some action, this hook that tell you what has happened in syberpay")
    # requests.post('YOUR_RETURN_HOOK', json={})
    return {"NEXT_ACTION": "Call other website url hook who need to be notified by the customer action"}

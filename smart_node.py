from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from smart_node_models.models import *

# import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

storage = {}


@app.post("/payment", response_model=PaymentResponse)
async def purchase_card_url(payment_request: PaymentRequest):
    # print("Payment Request: ", payment_request)
    if payment_request.card == "2222222222222222":
        return PaymentResponse(**{
            "status": True
        })
    if payment_request.card == "4444444444444444":
        return PaymentResponse(**{
            "status": False,
            "msg": "No credit, Standard EBS Response"
        })
    else:
        return PaymentResponse(**{
            "status": False,
            "msg": "Standard EBS Error Response"
        })

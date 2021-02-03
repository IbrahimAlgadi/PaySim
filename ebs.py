from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from ebs_models.models import *

# import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

storage = {}


@app.post("/purchase/card", response_model=PurchaseSaleCardResponse)
async def purchase_card_url(purchase_sale_request: PurchaseSaleCardRequest):
    print("Purchase Sale Request: ", purchase_sale_request)
    return PurchaseSaleCardResponse(**{
        "clientId": "string",
        "terminalId": "string",
        "transDateTime": "string",
        "systemTraceAuditNumber": "string",
        "tranCurrencyCode": "string",
        "tranAmount": "string",
        "additionalAmount": "string",
        "PAN": "string",
        "tranFee": "string",
        "referenceNumber": "string",
        "responseCode": "string",
        "responseMessage": "string",
        "responseStatus": "string",
        "approvalCode": "string"
    })


@app.post("/purchase/mobile_wallet", response_model=PurchaseSaleMobileWalletResponse)
async def purchase_mobile_wallet_url(purchase_sale_request: PurchaseSaleCardRequest):
    print("Purchase Sale Request: ", purchase_sale_request)
    return PurchaseSaleMobileWalletResponse(**{
        "tranFee": "string",
        "referenceNumber": "string",
        "responseCode": "string",
        "responseMessage": "string",
        "responseStatus": "string",
        "approvalCode": "string",
        "clientId": "string",
        "terminalId": "string",
        "transDateTime": "string",
        "systemTraceAuditNumber": "string",
        "tranCurrencyCode": "string",
        "tranAmount": "string",
        "additionalAmount": "string",
        "mobileNumber": "string"
    })


@app.post("/purchase/cash_back", response_model=PurchaseWithCashBackResponse)
async def purchase_cash_back_url(purchase_cash_back_request: PurchaseWithCashBackRequest):
    print("Purchase Sale Request: ", purchase_cash_back_request)
    return PurchaseWithCashBackResponse(**{
        "tranFee": "string",
        "referenceNumber": "string",
        "responseCode": "string",
        "responseMessage": "string",
        "responseStatus": "string",
        "approvalCode": "string",
        "clientId": "string",
        "terminalId": "string",
        "transDateTime": "string",
        "systemTraceAuditNumber": "string",
        "tranCurrencyCode": "string",
        "tranAmount": "string",
        "additionalAmount": "string",
        "PAN": "string",
        "cashBackAmount": "string"
    })


@app.post("/reversal", response_model=ReversalResponse)
async def reversal_url(purchase_cash_back_request: ReversalRequest):
    print("Purchase Sale Request: ", purchase_cash_back_request)
    return ReversalResponse(**{
        "tranFee": "string",
        "referenceNumber": "string",
        "responseCode": "string",
        "responseMessage": "string",
        "responseStatus": "string",
        "approvalCode": "string",
        "clientId": "string",
        "terminalId": "string",
        "transDateTime": "string",
        "systemTraceAuditNumber": "string",
        "tranCurrencyCode": "string",
        "tranAmount": "string",
        "additionalAmount": "string",
        "PAN": "string",
        "originalTranSystemTraceAuditNumber": "string",
        "serviceId": "string"
    })


@app.post("/mini_statement", response_model=MiniStatementResponse)
async def mini_statement_url(purchase_cash_back_request: MiniStatementRequest):
    print("Purchase Sale Request: ", purchase_cash_back_request)
    return MiniStatementResponse(**{
        "tranFee": "string",
        "referenceNumber": "string",
        "responseCode": "string",
        "responseMessage": "string",
        "responseStatus": "string",
        "approvalCode": "string",
        "tranAmount": "string",
        "additionalAmount": "string",
        "clientId": "string",
        "terminalId": "string",
        "transDateTime": "string",
        "systemTraceAuditNumber": "string",
        "tranCurrencyCode": "string",
        "PAN": "string"
    })


@app.post("/bill_inquiry", response_model=BillInquiryResponse)
async def bill_inquiry_url(purchase_cash_back_request: BillInquiryRequest):
    print("Purchase Sale Request: ", purchase_cash_back_request)
    return BillInquiryResponse(**{
        "tranFee": "string",
        "referenceNumber": "string",
        "responseCode": "string",
        "responseMessage": "string",
        "responseStatus": "string",
        "approvalCode": "string",
        "tranAmount": "string",
        "additionalAmount": "string",
        "clientId": "string",
        "terminalId": "string",
        "transDateTime": "string",
        "systemTraceAuditNumber": "string",
        "tranCurrencyCode": "string",
        "PAN": "string",
        "personalPaymentInfo": "string",
        "payeeId": "string"
    })

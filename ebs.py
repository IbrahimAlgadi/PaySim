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
        "payeeId": "string",
        "additionalData": "string"
    })


@app.post("/bill_payment", response_model=BillPaymentResponse)
async def bill_payment_url(purchase_cash_back_request: BillPaymentRequest):
    print("Purchase Sale Request: ", purchase_cash_back_request)
    return BillPaymentResponse(**{
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
        "additionalData": "string"
    })


@app.post("/pre_pay_payment", response_model=PrePayPaymentResponse)
async def pre_pay_payment_url(request: PrePayPaymentRequest):
    print("Request: ", request)
    return PrePayPaymentResponse(**{
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
        "additionalData": "string"
    })


@app.post("/balance_inquiry", response_model=BalanceInquiryResponse)
async def balance_inquiry_url(request: BalanceInquiryRequest):
    print("Request: ", request)
    return BalanceInquiryResponse(**{
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
        "additionalData": "string"
    })


@app.post("/pin_change", response_model=PinChangeResponse)
async def pin_change_url(request: PinChangeRequest):
    print("Request: ", request)
    return PinChangeResponse(**{
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
        "PAN": "string"
    })


@app.post("/cash_in", response_model=CashInResponse)
async def cash_in_url(request: CashInRequest):
    print("Request: ", request)
    return CashInResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "PAN": "string"
    })


@app.post("/refund", response_model=RefundResponse)
async def refund_url(request: RefundRequest):
    print("Request: ", request)
    return RefundResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "PAN": "string"
    })


@app.post("/generate_voucher", response_model=GenerateVoucherResponse)
async def generate_voucher_url(request: GenerateVoucherRequest):
    print("Request: ", request)
    return GenerateVoucherResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "phoneNumber": "string",
        "voucherNumber": "string"
    })


@app.post("/voucher_cash_out", response_model=VoucherCashOutResponse)
async def voucher_cash_out_url(request: VoucherCashOutRequest):
    print("Request: ", request)
    return VoucherCashOutResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "tranCurrencyCode": "string"
    })


@app.post("/voucher_cash_out_with_amount", response_model=VoucherCashOutWithAmountResponse)
async def voucher_cash_out_with_amount_url(request: VoucherCashOutWithAmountRequest):
    print("Request: ", request)
    return VoucherCashOutWithAmountResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "tranCurrencyCode": "string"
    })


@app.post("/card_transfer", response_model=CardTransferResponse)
async def card_transfer_url(request: CardTransferRequest):
    print("Request: ", request)
    return CardTransferResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "fromCard": "string"
    })


@app.post("/account_transfer", response_model=AccountTransferResponse)
async def account_transfer_url(request: AccountTransferRequest):
    print("Request: ", request)
    return AccountTransferResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "PAN": "string",
        "fromAccount": "string",
        "toAccount": "string"
    })


@app.post("/voucher_cash_in", response_model=VoucherCashInResponse)
async def voucher_cash_in_url(request: VoucherCashInRequest):
    print("Request: ", request)
    return VoucherCashInResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "PAN": "string",
        "DisputeRRN": "string",
        "toAccount": "string"
    })


@app.post("/network_test", response_model=NetworkTestResponse)
async def network_test_url(request: NetworkTestRequest):
    print("Request: ", request)
    return NetworkTestResponse(**{
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
        "tranCurrencyCode": "string"
    })


@app.post("/payees_list", response_model=PayeesListResponse)
async def payees_list_url(request: PayeesListRequest):
    print("Request: ", request)
    return PayeesListResponse(**{
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
        "payeesList": [
            {
                "payeeName": "MTN Top Up3",
                "payeeId": "0010010003"
            },
            {
                "payeeName": "SUDANI Bill Payment",
                "payeeId": "0010010006"
            },
            {
                "payeeName": "Zain Bill Payment",
                "payeeId": "0010010002"
            }
        ]
    })


@app.post("/working_key", response_model=WorkingKeyResponse)
async def working_key_url(request: WorkingKeyRequest):
    print("Request: ", request)
    return WorkingKeyResponse(**{
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
        "workingKey": "string"
    })


@app.post("/cash_out", response_model=CashOutResponse)
async def cash_out_url(request: CashOutRequest):
    print("Request: ", request)
    return CashOutResponse(**{
        "tranAmount": "string",
        "additionalAmount": "string",
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
        "PAN": "string"
    })

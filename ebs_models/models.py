from pydantic import BaseModel
from typing import Optional


# Payment Request
class MobileInfo(BaseModel):
    mobileNumber: str
    PIN: str


class CardInfo(BaseModel):
    PAN: str
    PIN: str
    expDate: str


class TransactionInfo(BaseModel):
    clientId: str
    terminalId: str
    transDateTime: str
    systemTraceAuditNumber: str
    tranCurrencyCode: str
    tranAmount: str
    additionalAmount: str


class TransactionStatusInfo(BaseModel):
    tranFee: str
    referenceNumber: str
    responseCode: str
    responseMessage: str
    responseStatus: str
    approvalCode: str


# Card
class PurchaseSaleCardRequest(CardInfo, TransactionInfo):
    pass


class PurchaseSaleCardResponse(TransactionInfo, TransactionStatusInfo):
    PAN: str


# Mobile
class PurchaseSaleMobileWalletRequest(MobileInfo, TransactionInfo):
    pass


class PurchaseSaleMobileWalletResponse(TransactionInfo, TransactionStatusInfo):
    mobileNumber: str


# Cashback
class PurchaseWithCashBackRequest(CardInfo, TransactionInfo):
    cashBackAmount: str


class PurchaseWithCashBackResponse(PurchaseSaleCardResponse):
    cashBackAmount: str


# Reversal
class ReversalRequest(TransactionInfo):
    PAN: str
    expDate: str
    originalTranSystemTraceAuditNumber: str
    serviceId: str


class ReversalResponse(PurchaseSaleCardResponse):
    originalTranSystemTraceAuditNumber: str
    serviceId: str

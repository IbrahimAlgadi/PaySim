from pydantic import BaseModel
from typing import Optional


# Payment Request
class PaymentInfo(BaseModel):
    accountNo: str
    customerName: str
    serviceType: str


class PaymentRequest(BaseModel):
    applicationId: str
    payeeId: str
    serviceId: str
    customerRef: str
    currency: str
    amount: int
    paymentInfo: Optional[PaymentInfo]
    hash: str


class InitiatePayment(BaseModel):
    applicationId: str
    payeeId: str
    serviceId: str
    amount: int
    currency: str
    customerRef: str
    tranTimestamp: str
    paymentInfo: Optional[PaymentInfo]
    responseCode: int
    responseMessage: str
    paymentUrl: str


# Payment Status Response
class PaymentStatusReq(BaseModel):
    applicationId: str
    transactionId: str
    hash: str


class ResponseData(BaseModel):
    receiptNo: str


class Payment(BaseModel):
    applicationId: str
    payeeId: str
    serviceId: str
    amount: int
    currency: str
    customerRef: str
    tranTimestamp: str
    paymentInfo: Optional[PaymentInfo]
    responseData: ResponseData
    responseCode: int
    responseMessage: str
    status: str


class PaymentStatusResp(BaseModel):
    status: str
    responseCode: int
    responseMessage: str
    payment: Payment

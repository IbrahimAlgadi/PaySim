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


class TransactionAmountInfo(BaseModel):
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
class PurchaseSaleCardRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    pass


class PurchaseSaleCardResponse(TransactionInfo, TransactionAmountInfo, TransactionStatusInfo):
    PAN: str


# Mobile
class PurchaseSaleMobileWalletRequest(MobileInfo, TransactionInfo, TransactionAmountInfo):
    pass


class PurchaseSaleMobileWalletResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    mobileNumber: str


# Cashback
class PurchaseWithCashBackRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    cashBackAmount: str


class PurchaseWithCashBackResponse(PurchaseSaleCardResponse):
    cashBackAmount: str


# Reversal
class ReversalRequest(TransactionInfo, TransactionAmountInfo):
    PAN: str
    expDate: str
    originalTranSystemTraceAuditNumber: str
    serviceId: str


class ReversalResponse(PurchaseSaleCardResponse):
    originalTranSystemTraceAuditNumber: str
    serviceId: str


# Mini Statement
class MiniStatementRequest(CardInfo, TransactionInfo):
    pass


class MiniStatementResponse(PurchaseSaleCardResponse):
    pass


# Bill Payment
class BillInquiryRequest(CardInfo, TransactionInfo):
    personalPaymentInfo: str
    payeeId: str


class BillInquiryResponse(PurchaseSaleCardResponse):
    personalPaymentInfo: str
    payeeId: str
    additionalData: str


# Bill Payment
class BillPaymentRequest(BillInquiryRequest, TransactionAmountInfo):
    pass


class BillPaymentResponse(PurchaseSaleCardResponse):
    additionalData: str


# Bill Payment
class PrePayPaymentRequest(BillInquiryRequest, TransactionAmountInfo):
    pass


class PrePayPaymentResponse(PurchaseSaleCardResponse):
    additionalData: str


# Bill Inquiry
class BalanceInquiryRequest(CardInfo, TransactionInfo):
    tranCurrencyCode: Optional[str]


class BalanceInquiryResponse(TransactionInfo, TransactionAmountInfo, TransactionStatusInfo):
    additionalData: str


# PIN Change
class PinChangeRequest(CardInfo, TransactionInfo):
    newPIN: str


class PinChangeResponse(TransactionInfo, TransactionStatusInfo):
    PAN: str


# Cash In
class CashInRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    newPIN: str


class CashInResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    PAN: str


# Refund
class RefundRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    newPIN: str


class RefundResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    PAN: str


# Generate Voucher
class GenerateVoucherRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    phoneNumber: str


class GenerateVoucherResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    phoneNumber: str
    voucherNumber: str


# Voucher Cash Out (Depricated)
class VoucherCashOutRequest(CardInfo, TransactionInfo):
    phoneNumber: str
    voucherNumber: str


class VoucherCashOutResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    pass


#  Voucher Cash Out With Amount (Depricated)
class VoucherCashOutWithAmountRequest(CardInfo, TransactionInfo):
    phoneNumber: str
    voucherNumber: str
    tranAmount: str


class VoucherCashOutWithAmountResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    tranAmount: str


#  Card Transfer
class CardTransferRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    toCard: str


class CardTransferResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    fromCard: str


#  Card Transfer
class AccountTransferRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    toAccount: str
    accountType: str


class AccountTransferResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    PAN: str
    fromAccount: str
    toAccount: str


#  Voucher Cash In
class VoucherCashInRequest(CardInfo, TransactionInfo, TransactionAmountInfo):
    approvalCode: str
    voucherNumber: str


class VoucherCashInResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    PAN: str
    DisputeRRN: str
    toAccount: str


#  Network Test
class NetworkTestRequest(TransactionInfo):
    pass


class NetworkTestResponse(TransactionInfo, TransactionStatusInfo):
    pass


#  Payees List
class PayeesListRequest(TransactionInfo):
    pass


class PayeesListResponse(TransactionInfo, TransactionStatusInfo):
    payeesList: str


#  Working Key Request
class WorkingKeyRequest(TransactionInfo):
    pass


class WorkingKeyResponse(TransactionInfo, TransactionStatusInfo):
    workingKey: str


#  Working Key Request
class CashOutRequest(TransactionInfo, TransactionAmountInfo):
    pass


class CashOutResponse(TransactionInfo, TransactionStatusInfo, TransactionAmountInfo):
    PAN: str

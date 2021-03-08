from pydantic import BaseModel


from typing import Optional, List


# Payment Request
class AccessInfo(BaseModel):
    user: str
    token: str


class CardInfo(BaseModel):
    card: str
    amount: str
    expDate: str
    pin: str


class PaymentRequest(AccessInfo, CardInfo):
    pass


class PaymentResponse(BaseModel):
    status: bool
    msg: Optional[str]

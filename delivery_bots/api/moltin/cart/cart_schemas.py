from pydantic import BaseModel


class Links(BaseModel):
    self: str


class DisplayPriceWithTax(BaseModel):
    amount: int
    currency: str
    formatted: str


class DisplayPriceWithoutTax(BaseModel):
    amount: int
    currency: str
    formatted: str


class DisplayPrice(BaseModel):
    with_tax: DisplayPriceWithTax
    without_tax: DisplayPriceWithoutTax


class Meta(BaseModel):
    display_price: DisplayPrice


class CartDatum(BaseModel):
    id: str
    type: str
    links: Links
    meta: Meta


class Cart(BaseModel):
    data: CartDatum

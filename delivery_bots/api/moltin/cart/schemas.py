from pydantic import BaseModel


class Image(BaseModel):
    mime_type: str
    file_name: str
    href: str


class CartUnitPrice(BaseModel):
    amount: int
    currency: str
    includes_tax: bool


class CartValue(BaseModel):
    amount: int
    currency: str
    includes_tax: bool


class Links(BaseModel):
    product: str


class Unit(BaseModel):
    amount: int
    currency: str
    formatted: str


class Value(BaseModel):
    amount: int
    currency: str
    formatted: str


class DisplayPriceTax(BaseModel):
    unit: Unit
    value: Value


class DisplayPrice(BaseModel):
    with_tax: DisplayPriceTax
    without_tax: DisplayPriceTax


class Meta(BaseModel):
    display_price: DisplayPrice


class CartProduct(BaseModel):
    id: str
    type: str
    product_id: str
    name: str
    description: str
    sku: str
    image: Image
    quantity: int
    manage_stock: bool
    unit_price: CartUnitPrice
    value: CartValue
    links: Links
    meta: Meta

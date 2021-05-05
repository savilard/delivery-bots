from typing import Optional

from pydantic import BaseModel


class TaxPrice(BaseModel):
    amount: int
    currency: str
    formatted: str


class DisplayPrice(BaseModel):
    with_tax: TaxPrice
    without_tax: TaxPrice


class Stock(BaseModel):
    availability: str
    level: int


class Meta(BaseModel):
    display_price: DisplayPrice
    stock: Stock


class Image(BaseModel):
    type: str
    id: str


class ImageData(BaseModel):
    data: Image


class Relationships(BaseModel):
    main_image: Optional[ImageData]


class CatalogProduct(BaseModel):
    type: str
    id: str
    status: str
    name: str
    slug: str
    sku: str
    description: str
    meta: Meta
    relationships: Optional[Relationships]

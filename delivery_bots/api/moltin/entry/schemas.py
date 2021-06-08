from pydantic import BaseModel


class Timestamps(BaseModel):
    created_at: str
    updated_at: str


class Meta(BaseModel):
    timestamps: Timestamps


class Links(BaseModel):
    self: str


class Entry(BaseModel):
    id: str
    type: str
    address: str
    alias: str
    longitude: str
    latitude: str
    deliveryman_tg_id: str
    meta: Meta
    links: Links

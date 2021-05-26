from pydantic import BaseModel


class Link(BaseModel):
    href: str


class Links(BaseModel):
    self: str


class Dimensions(BaseModel):
    width: int
    height: int


class Timestamps(BaseModel):
    created_at: str


class Meta(BaseModel):
    dimensions: Dimensions
    timestamps: Timestamps


class MoltinFileData(BaseModel):
    type: str
    id: str
    link: Link
    file_name: str
    mime_type: str
    file_size: int
    public: bool
    meta: Meta
    links: Links


class MoltinFile(BaseModel):
    data: MoltinFileData

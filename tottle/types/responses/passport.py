from typing import Optional, List

from pydantic import BaseModel


class PassportFile(BaseModel):
    file_id: str
    file_unique_id: str

    file_size: int
    file_date: int


class EncryptedPassportElement(BaseModel):
    type: str
    data: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    files: Optional[List[PassportFile]] = None

    front_side: Optional[PassportFile] = None
    reverse_side: Optional[PassportFile] = None
    selfie: Optional[PassportFile] = None
    translation: Optional[PassportFile] = None

    hash: str


class EncryptedCredentials(BaseModel):
    data: str
    hash: str
    secret: str


class PassportData(BaseModel):
    data: List[EncryptedPassportElement]
    credentials: EncryptedCredentials

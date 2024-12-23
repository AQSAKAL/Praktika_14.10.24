from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from decimal import Decimal
from datetime import datetime

# Определяем Enum для типа транзакции
class TransactionType(str, Enum):
    sale = 'sale'
    purchase = 'purchase'

# Базовая схема для модели Item
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    grade: Optional[str] = None
    active: bool
    sku: Optional[str] = None
    count: int
    image_url: Optional[str] = None
    price: Decimal
    transaction_type: TransactionType

# Схема для создания записи Item
class ItemCreate(ItemBase):
    user_id: int

# Схема для обновления записи Item
class ItemUpdate(ItemBase):
    name: Optional[str] = None
    count: Optional[int] = None

# Схема для отображения записи Item (например, в ответах API)
class ItemResponse(ItemBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    surname: str
    email: str
    password: str  # Пароль, который будем хэшировать перед сохранением
    verified: Optional[bool] = False
    active: Optional[bool] = True

class ContractCreate(BaseModel):
    item_id: int
    buyer_user_id: int
    seller_user_id: int
    signed: bool = False
    total_value: Decimal

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

class PaymentCreate(BaseModel):
    received: bool
    status: List[PaymentStatus]
    contract_id: int


class UserBase(BaseModel):
    id: int
    name: str
    surname: str

    class Config:
        from_attributes = True
class ContractView(BaseModel):
    id: int
    item: ItemBase
    buyer: UserBase
    seller: UserBase
    signed: bool
    created_at: datetime
    updated_at: datetime
    total_value: Decimal

    class Config:
        from_attributes = True
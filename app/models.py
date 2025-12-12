from enum import Enum
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, date, time
from pydantic import BaseModel # Used in template, though SQLModel is enough

# --- Enums ---
class UserRole(str, Enum):
    admin = "admin"
    user = "user"
    shelter = "shelter"

class AnimalSize(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"

class AnimalStatus(str, Enum):
    available = "available"
    adopted = "adopted"
    reserved = "reserved"
    other = "other"

# --- USERS ---

class UserBase(SQLModel):
    name: str
    email: str
    role: UserRole
    location: str

class UserIn(UserBase):
    password: str

class UserDb(UserIn, table=True):
    __tablename__ = "user" #
    id: Optional[int] = Field(default=None, primary_key=True)
    # Relaciones
    managed_shelters: List["ShelterDb"] = Relationship(back_populates="admin_user")
    posts: List["PostDb"] = Relationship(back_populates="user_rel")
    

class UserOut(UserBase):
    id: int


class ShelterBase(SQLModel):
    name: str
    address: str
    contact: str
    website: str
    description: str

class ShelterIn(ShelterBase):
    pass

class ShelterDb(ShelterIn, table=True):
    __tablename__ = "shelter"
    id: Optional[int] = Field(default=None, primary_key=True)
    admin: int = Field(foreign_key="user.id")
    
    admin_user: UserDb = Relationship(back_populates="managed_shelters")
    animals: List["AnimalDb"] = Relationship(back_populates="shelter_rel")

class ShelterOut(ShelterBase):
    id: int
    admin: int

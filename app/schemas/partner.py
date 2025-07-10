"""
Partner schemas for data validation and serialization.

This module contains Pydantic models for partner-related data structures,
ensuring proper data validation and serialization/deserialization.
"""

from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class PartnerBase(BaseModel):
    """
    Base schema for Partner with common attributes.

    Attributes:
        name: The partner's full name
        email: Optional email address
        phone: Optional phone number in international format
    """

    name: constr(min_length=1, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class PartnerCreate(PartnerBase):
    """Schema for creating a new partner."""

    pass


class PartnerUpdate(PartnerBase):
    """Schema for updating an existing partner."""

    name: Optional[constr(min_length=1, max_length=255)] = None


class Partner(PartnerBase):
    """
    Schema for partner response including database id.

    Attributes:
        id: The unique identifier for the partner
    """

    id: int

    class Config:
        """Pydantic config for the Partner model."""

        from_attributes = True

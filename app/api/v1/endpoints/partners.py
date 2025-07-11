from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException

from ....core.constants import PARTNER_FIELDS
from ....core.security import get_current_user
from ....schemas.partner import Partner
from ....services.odoo import odoo

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("", response_model=List[Partner])
async def get_partners(limit: int = 10) -> List[Dict]:
    """
    Get partners from Odoo.

    Retrieves a list of company partners from Odoo.

    Args:
        limit: Maximum number of partners to return (default: 10)

    Returns:
        List[Partner]: List of partners

    Raises:
        HTTPException: If there's an error fetching partners from Odoo
    """
    partners = await odoo.fetch_records(
        model="res.partner",
        domain=[],
        fields=PARTNER_FIELDS,
        limit=limit,
    )
    return partners


@router.get("/{partner_id}", response_model=Partner)
async def get_partner(partner_id: int) -> Dict:
    """
    Get a single partner from Odoo.

    Retrieves a specific partner by their ID.

    Args:
        partner_id: The unique identifier of the partner

    Returns:
        Partner: The requested partner

    Raises:
        HTTPException: If the partner is not found or there's an error fetching from Odoo
    """
    partners = await odoo.fetch_records(
        model="res.partner", domain=[["id", "=", partner_id]], fields=PARTNER_FIELDS
    )

    if not partners:
        raise HTTPException(status_code=404, detail="Partner not found")

    return partners[0]

from typing import Any, Dict, List, Optional
from xmlrpc import client

from fastapi import HTTPException

from ..core.config import settings


class OdooService:
    def __init__(self):
        self.url = settings.odoo_url
        self.db = settings.odoo_db
        self.username = settings.odoo_username
        self.password = settings.odoo_password
        self._uid = None
        self._models = None

    def _connect(self):
        if not self._uid:
            common = client.ServerProxy(f"{self.url}/xmlrpc/2/common")
            self._uid = common.authenticate(self.db, self.username, self.password, {})
            if not self._uid:
                raise HTTPException(
                    status_code=401, detail="Odoo authentication failed"
                )

            self._models = client.ServerProxy(f"{self.url}/xmlrpc/2/object")

    async def fetch_records(
        self,
        model: str,
        domain: List[List],
        fields: List[str],
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """Generic function to fetch records from Odoo"""
        try:
            self._connect()
            kwargs = {"fields": fields}
            if limit:
                kwargs["limit"] = limit

            return self._models.execute_kw(
                self.db,
                self._uid,
                self.password,
                model,
                "search_read",
                [domain],
                kwargs,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


odoo = OdooService()

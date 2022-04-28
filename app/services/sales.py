from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_session
from app import models
from app.db import tables


class SalesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, sale_id: int) -> tables.Sale:
        sale = (
            self.session
                .query(tables.Sale)
                .filter_by(id=sale_id, user_id=user_id)
                .first()
        )
        if not sale:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return sale

    def get_list(self, user_id: int, region: Optional[models.RegionName] = None) -> List[tables.Sale]:
        query = self.session.query(tables.Sale).filter_by(user_id=user_id)
        if region:
            query = query.filter_by(region=region)
        sales = query.all()
        return sales

    def get(self, user_id: int, sale_id: int) -> tables.Sale:
        return self._get(user_id, sale_id)

    def get_many(self, user_id: int) -> List[tables.Sale]:
        sales = (self.session
                 .query(tables.Sale)
                 .filter(tables.Sale.user_id == user_id)
                 .order_by(
            tables.Sale.date.desc(),
            tables.Sale.id.desc(),
        )
                 .all()
                 )
        return sales

    def create(self, user_id: int, sale_data: models.SaleCreate) -> tables.Sale:
        sale = tables.Sale(**sale_data.dict(), user_id=user_id)
        self.session.add(sale)
        self.session.commit()
        return sale

    def create_many(self, user_id: int, sales_data: List[models.SaleCreate]) -> List[tables.Sale]:
        sales = [
            tables.Sale(**sale_data.dict(), user_id=user_id) for sale_data in sales_data
        ]
        self.session.add_all(sales)
        self.session.commit()
        return sales

    def update(self, user_id: int, sale_id: int, sale_data: models.SaleUpdate) -> tables.Sale:
        sale = self._get(user_id, sale_id)
        for field, value in sale_data:
            setattr(sale, field, value)
        self.session.commit()
        return sale

    def delete(self, user_id: int, sale_id: int):
        sale = self._get(user_id, sale_id)
        self.session.delete(sale)
        self.session.commit()

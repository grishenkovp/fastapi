import csv
from io import StringIO
from typing import (
    BinaryIO,
    TextIO,
)

from fastapi import Depends

from app.services.sales import SalesService
from app import models


class ReportsService:
    report_fields = [
        'date',
        'region',
        'product',
        'unit_price',
        'quantity',
        'amount',
        'description',
    ]

    def __init__(self, sales_service: SalesService = Depends()):
        self.sales_service = sales_service

    def import_csv(self, user_id: int, file: BinaryIO):
        reader = csv.DictReader(
            (line.decode() for line in file),
            fieldnames=self.report_fields,
        )
        next(reader, None)
        sales_data = []
        for row in reader:
            sale_data = models.SaleCreate.parse_obj(row)
            if sale_data.description == '':
                sale_data.description = None
            sales_data.append(sale_data)
        self.sales_service.create_many(
            user_id,
            sales_data,
        )

    def export_csv(self, user_id: int) -> TextIO:
        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=self.report_fields,
            extrasaction='ignore',
        )

        sales = self.sales_service.get_many(user_id)

        writer.writeheader()
        for sale in sales:
            sale_data = models.Sale.from_orm(sale)
            writer.writerow(sale_data.dict())

        output.seek(0)
        return output

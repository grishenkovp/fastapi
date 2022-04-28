from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status
)

from app import models
from app.services.auth import get_current_user
from app.services.sales import SalesService

router = APIRouter(
    prefix='/sales',
    tags=['sales'],
)


@router.get('/', response_model=List[models.Sale])
def get_sales(region: Optional[models.RegionName] = None,
              user: models.User = Depends(get_current_user),
              service: SalesService = Depends()):
    return service.get_list(region=region, user_id=user.id)


@router.post('/', response_model=models.Sale)
def create_sale(sale_data: models.SaleCreate,
                user: models.User = Depends(get_current_user),
                service: SalesService = Depends()):
    return service.create(sale_data=sale_data, user_id=user.id)


@router.get('/{sale_id}', response_model=models.Sale)
def get_sale(sale_id: int,
             user: models.User = Depends(get_current_user),
             service: SalesService = Depends()):
    return service.get(sale_id=sale_id, user_id=user.id)


@router.put('/{sale_id}', response_model=models.Sale)
def update_sale(sale_id: int,
                sale_data: models.SaleUpdate,
                user: models.User = Depends(get_current_user),
                service: SalesService = Depends()):
    return service.update(sale_id=sale_id, sale_data=sale_data, user_id=user.id)


@router.delete('/{sale_id}')
def delete_sale(sale_id: int,
                user: models.User = Depends(get_current_user),
                service: SalesService = Depends()):
    service.delete(sale_id=sale_id, user_id=user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

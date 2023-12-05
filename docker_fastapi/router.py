from typing import Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from docker_fastapi.dao import engine
from .models import Installation, Base
from sqlalchemy.orm import Session
from .dao import get_db
from .schemas import Installations

installations_router = APIRouter(prefix="/installations", tags=["Sites Installations"])

Base.metadata.create_all(bind=engine)


## TODO: Add a service layer for the business logic with a simple repository pattern
## TODO: Add a new endpoint for the service layer


class QueryParams(BaseModel):
    name: Optional[str] = None
    id: Optional[int] = None


@installations_router.get("/ping")
def ping():
    return {"ping": "pong"}


@installations_router.get("/foo_parameters")
def products(query_params: QueryParams = Depends()):
    name = query_params.name
    product_id = query_params.id
    return {"name": name, "id": product_id}


@installations_router.post("/installation")
def create_installation(installation: Installations, db: Session = Depends(get_db)) -> Installations:
    new_installation = Installation(**installation.model_dump())
    db.add(new_installation)
    db.commit()
    db.refresh(new_installation)
    return new_installation


@installations_router.get("/installation")
def get_installation(db: Session = Depends(get_db)):
    all_installations = db.query(Installation).all()
    return all_installations


@installations_router.get("/installation/{id}")
def get_installation_by_id(installation_id: int, db: Session = Depends(get_db)):
    installation = db.query(Installation).filter(Installation.id == installation_id).first()
    return installation


@installations_router.delete("/installation/{id}")
def delete_installation(installation_id: int, db: Session = Depends(get_db)):
    installation = db.query(Installation).filter(Installation.id == installation_id).first()
    db.delete(installation)
    db.commit()
    return {"message": "Installation deleted successfully"}


@installations_router.put("/installation/{id}")
def update_installation(installation_id: int, installation: Installations, db: Session = Depends(get_db)):
    old_installation = db.query(Installation).filter(Installation.id == installation_id).first()
    old_installation.device_name = installation.device_name
    old_installation.description = installation.description
    old_installation.status = installation.status
    old_installation.updated_at = installation.updated_at
    db.commit()
    db.refresh(old_installation)
    return {"message": "Installation updated successfully"}

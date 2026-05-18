from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate
from typing import List, Optional

router = APIRouter(prefix="/applications", tags=["applications"])

@router.get("/", response_model=List[ApplicationResponse])
async def get_applications(
    status: Optional[str] = None,
    company: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Application)

    if status:
        query = query.where(Application.status == status)

    if company:
        query = query.where(Application.company.ilike(f"%{company}%"))

    result = await db.execute(query)

    return result.scalars().all()

@router.post("/", response_model=ApplicationResponse, status_code=201)
async def create_application(
    payload: ApplicationCreate,
    db: AsyncSession = Depends(get_db)
):
    application = Application(**payload.model_dump())

    db.add(application)
    await db.commit()
    await db.refresh(application)

    return application

@router.get("/{id}", response_model=ApplicationResponse)
async def get_application(
    id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Application).where(Application.id == id))

    application = result.scalar_one_or_none()

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    return application


@router.put("/{id}", response_model=ApplicationResponse)
async def update_application(id: int, payload: ApplicationUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Application).where(Application.id == id))

    application = result.scalar_one_or_none()

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    for key, value in payload.model_dump().items():
        setattr(application, key, value)

    await db.commit()
    await db.refresh(application)

    return application

@router.delete("/{id}", status_code=204)
async def delete_application(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Application).where(Application.id == id))

    application = result.scalar_one_or_none()

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    await db.delete(application)
    await db.commit()

    return {"message": "Successfully deleted Application"}


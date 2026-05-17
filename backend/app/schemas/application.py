from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ApplicationBase(BaseModel):
    company: str
    role: str
    status: str = "applied"
    date_applied: date
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    job_url: Optional[str] = None
    notes: Optional[str] = None
    contact_name: Optional[str] = None
    contact_email: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(ApplicationBase):
    pass


class ApplicationResponse(ApplicationBase):
    id: int
    create_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
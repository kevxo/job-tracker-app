from sqlalchemy import Column, Integer, String, Text, Date, DateTime
from sqlalchemy.sql import func
from database import Base


class Application(Base):
    __tablename__ = "applications"

    id            = Column(Integer, primary_key=True, index=True)
    company       = Column(String(100), nullable=False)
    role          = Column(String(100), nullable=False)
    status        = Column(String(50), nullable=False, default="applied")
    date_applied  = Column(Date, nullable=False)
    salary_min    = Column(Integer, nullable=True)
    salary_max    = Column(Integer, nullable=True)
    job_url       = Column(Text, nullable=True)
    notes         = Column(Text, nullable=True)
    contact_name  = Column(String(100), nullable=True)
    contact_email = Column(String(100), nullable=True)
    created_at    = Column(DateTime(timezone=True), server_default=func.now())
    updated_at    = Column(DateTime(timezone=True), onupdate=func.now())

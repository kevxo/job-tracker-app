from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.applications import router as application_router
from app.database import engine, Base

app = FastAPI(title="Job Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(application_router)

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.applications import router as applications_router
from app.lifespan import lifespan

app = FastAPI(title="Job Tracker API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(applications_router)

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}
from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine
from app.api.auth import router as auth_router


app = FastAPI(
    title="HireAI API",
    description="AI-powered recruitment and candidate management platform",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to HireAI API"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "message": "HireAI backend is running"
    }

@app.get("/api/database-test")
def database_test():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "PostgreSQL connection successful"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
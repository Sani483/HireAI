from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
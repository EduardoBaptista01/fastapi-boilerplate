from fastapi import FastAPI, HTTPException
from models import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routes.todos import router as todos_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Dependency function for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Return DB session
    finally:
        db.close()  # Ensure it closes after request

app.include_router(todos_router)

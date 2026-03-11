from fastapi import FastAPI
from pydantic import BaseModel
from model.model import check_prime

app = FastAPI()

# FastAPI uses Pydantic models to validate data.
class MessageIn(BaseModel):
    """Input model for integer.
    FastAPI checks the type of the input."""
    number: int

# FastAPI uses Pydantic models to validate data.
class BoolOut(BaseModel):
    """Output model for boolean."""
    is_prime: bool

@app.get("/")
def home():
    return {"health_check": "ok"}

@app.post("/check_prime", response_model=BoolOut)
def check_prime_endpoint(payload: MessageIn):
    is_prime = check_prime(payload.number) # input
    return {"is_prime": is_prime}
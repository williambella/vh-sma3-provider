from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/users/{user_id}")
def get_user(user_id: int):
    """Return a user by id."""
    return {"id": user_id}


@app.post("/api/v1/orders")
def create_order(payload: dict):
    """Create an order."""
    return {"ok": True}


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}

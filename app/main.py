from fastapi import FastAPI
from .api.endpoints import endpoints_router


app = FastAPI(title="FastAPI Template")
app.include_router(endpoints_router, prefix="/api", tags=["api"])


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
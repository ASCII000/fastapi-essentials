"""
Main module for run app
"""

from fastapi import FastAPI

from setup import setup
from dependencies.lifespan import lifespan


app = FastAPI(
    lifespan=lifespan,
    title=setup.API_NAME,
    description=setup.API_DESCRIPTION,
    version="1.0.0",
)


from domain.admin.auth.routers import router as auth_router
app.include_router(auth_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

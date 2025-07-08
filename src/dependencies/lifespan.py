"""
Module contains lifecycle for app
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from setup import setup


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Method of lifecycle for app

    Notes:
        The method manager the database connection session
    """

    # Create the database session
    engine = await setup.create_relational_db_engine()
    async_db_session = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    # Create the database session in state app
    app.state.db_session = async_db_session

    yield

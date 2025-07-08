"""
Module for authentications routers
"""

from fastapi import APIRouter


router = APIRouter()


@router.get("/me")
async def me():
    pass


@router.post("/login")
async def login():
    pass


@router.post("/logout")
async def logout():
    pass


@router.post("/refresh")
async def refresh():
    pass


@router.post("/revoke")
async def revoke():
    pass


@router.post("/register")
async def register():
    pass

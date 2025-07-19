"""
Models for authentication
"""

from pydantic import BaseModel, Field


class JWTToken(BaseModel):
    """
    JWT Token
    """
    access_token: str = Field(..., title="Access Token")
    refresh_token: str = Field(..., title="Refresh Token")

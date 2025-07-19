"""
Module for security
"""

import datetime

import hashlib

import jwt


class JWTManager:
    """
    Manager for JWT secrets
    """

    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def encode(self, payload: dict, expires_in_minutes: int) -> str:
        """
        Encode payload

        Args:
            payload (dict): Payload
            expires_in_minutes (int): Expiration in minutes
        
        Returns:
            str: Token encoded
        """
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=expires_in_minutes)
        payload["exp"] = expiration
        return jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm
        )

    def decode(self, token: str) -> dict:
        """
        Decode token

        Args:
            token (str): Token
        
        Returns:
            dict: Payload decoded
        """

        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])


def sha256_encrypt(text: str) -> str:
    """
    Encrypt text

    Args:
        text (str): The text without encryption
    
    Returns:
        str: Encrypted text
    """
    text_bytes = text.encode('utf-8')
    sha256_hash = hashlib.sha256(text_bytes)
    return sha256_hash.hexdigest()

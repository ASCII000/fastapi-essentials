"""
Raises for authentication
"""

class AuthenticationError(Exception):
    """
    Authentication error

    Args:
        reason (str): Error reason
    """

    def __init__(self, reason: str, *args):
        self.reason = reason
        super().__init__(*args)

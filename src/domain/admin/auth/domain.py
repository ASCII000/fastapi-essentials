"""
Domain of rules services for auth
"""

from fastapi import Request, Depends
from database.repositories import EmployeeRepository


class AuthDomain:
    """
    Class for auth domain
    """

    def __init__(self, request: Request, repository: EmployeeRepository = Depends(EmployeeRepository)):
        self.request = request
        self.repo = repository

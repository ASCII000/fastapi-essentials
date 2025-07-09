"""
Module contains class for password login
"""

from database.repositories import Employee
from utils.security import sha256_encrypt
from ..auth_raises import AuthenticationError
from ..auth_interfaces import PasswordLoginInputStrategyInterface


class PasswordLoginInputStrategy(PasswordLoginInputStrategyInterface):
    """
    Class for password login
    """

    async def login(self) -> Employee:
        """
        Verify login password and return employee
        """

        # Get employee by email
        employee = await self._repository.get_employee_by_email(self.username)

        # Verify if employee exists and passwords match
        if employee and employee.senha == sha256_encrypt(self.password):
            return employee

        raise AuthenticationError("Invalid email or password")

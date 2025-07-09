"""
Module for import employee repositories
"""

from fastapi import Depends

from database.tables import Employee
from dependencies.database import get_db_session, AsyncSession


class EmployeeRepository:
    """
    Class for employee repository
    """

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_employee(self, employee: Employee) -> Employee:
        """
        Create employee

        Args:
            employee (Funcionario): Employee

        Returns:
            Funcionario: Employee
        """

        self.session.add(employee)
        await self.session.flush()
        return employee

    async def get_employee_by_id(self, employee_id: int) -> Employee:
        """
        Get employee by id

        Args:
            employee_id (int): Employee id
        """
        return await self.session.get(Employee, employee_id)

    async def get_employee_by_email(self, email: str) -> Employee:
        """
        Get employee by email

        Args:
            email (str): Employee email
        """
        return await self.session.get(Employee, email)

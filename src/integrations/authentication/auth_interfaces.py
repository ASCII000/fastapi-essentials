"""
Interfaces for authentication
"""

from enum import Enum
from abc import ABC, abstractmethod

from pydantic import BaseModel, PrivateAttr

from database.repositories import EmployeeRepository
from utils.security import JWTManager
from database.tables import Employee
from .auth_models import JWTToken


class LoginStrategies(Enum):
    """
    Enum for login strategy
    """
    EMAIL_PASSWORD = "login-with-password"
    GOOGLE = "login-with-google"
    DISCORD = "login-with-discord"


class BaseLoginInputStrategy(BaseModel, ABC):
    """
    Base class for login strategy
    """
    _repository: EmployeeRepository = PrivateAttr()

    def __init__(self, repository: EmployeeRepository, **data):
        super().__init__(**data)
        self._repository = repository

    @property
    @abstractmethod
    def __strategy__(self) -> str:
        """
        Return login strategy
        """

    @abstractmethod
    async def login(self) -> Employee:
        """
        Return login tokens based on strategy

        Raises:
            AuthenticationError: Invalid credentials
        """


class PasswordLoginInputStrategyInterface(BaseLoginInputStrategy):
    """
    Class for password login
    """

    username: str
    password: str

    @property
    def __strategy__(self) -> str:
        return LoginStrategies.EMAIL_PASSWORD.value


class AuthenticationFactoryInterface(ABC):
    """
    Class for manager authentication adapters
    """

    def __init__(self, jwt_manager: JWTManager):
        self.jwt_manager = jwt_manager
        super().__init__()

    @abstractmethod
    async def login(self, input_strategy: BaseLoginInputStrategy) -> JWTToken:
        """
        Return login tokens based on strategy

        Args:
            input_strategy (BaseLoginInputStrategy): Login strategy
        
        Returns:
            JWTToken: Login tokens
        """

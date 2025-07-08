# pylint: disable=invalid-name, too-few-public-methods

"""
Module for import setup
"""

from typing import TypeVar, Type
import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from dotenv import dotenv_values


T = TypeVar("T")

class Setup:
    """
    Class contains the environment variables
    and database connection
    """

    def __init__(self):
        """
        Attrs:
            API_PORT : porta da api
            API_NAME: nome da api
            API_HOST: host da api
            API_DESCRIPTION: descricao da api
        """

        self.env = dotenv_values(".env")

        self.API_PORT = self.get_env("API_PORT", 8000, int)
        self.API_NAME = self.get_env("API_NAME", "API", str)
        self.API_HOST = self.get_env("API_HOST", "0.0.0.0", str)
        self.API_DESCRIPTION = self.get_env(
            "API_DESCRIPTION", "API Startup", str
        )

        self.MYSQL_DB_HOST = self.get_env("DB_HOST", "192.168.3.6", str)
        self.MYSQL_DB_PORT = self.get_env("DB_PORT", 4303, int)
        self.MYSQL_DB_USER = self.get_env("DB_USER", "root", str)
        self.MYSQL_DB_PASSWORD = self.get_env("DB_PASSWORD", "admin2024", str)
        self.MYSQL_DB_NAME = self.get_env("DB_NAME", "fastapi_essentials", str)

    async def create_relational_db_engine(self) -> AsyncEngine:
        """
        Create database engine
        """
        db_url = "mysql+aiomysql://{}:{}@{}:{}/{}".format(  # pylint: disable=consider-using-f-string
            self.MYSQL_DB_USER,
            self.MYSQL_DB_PASSWORD,
            self.MYSQL_DB_HOST,
            self.MYSQL_DB_PORT,
            self.MYSQL_DB_NAME,
        )

        engine = create_async_engine(db_url)
        return engine

    def get_env(
        self,
        value: str,
        default_value: str = None,
        type_value: Type[T] = str,
    ) -> T:
        """
        Get the value of the environment variable
        
        Args:
            value: The name of the environment variable
            default_value: The default value to use if the environment variable is not set
            type_value: The type of the environment variable
        """

        try:

            # Try to get the value of the environment variable
            result = self.env.get(value, default_value)
            return type_value(result) if result is not None else default_value

        except ValueError as err:

            # If not getter the value of the environment variable
            # return the default value case not default value
            # raise the error
            if default_value is None:
                raise ValueError(
                    "Variavel de ambiente nao compativel com o tipo "
                    f"esperado: {type_value.__name__}"
                ) from err

            logging.warning(
                "Variavel %s nao encontrada usando o valor padrao: %s",
                value, default_value
            )

            return default_value


setup = Setup()

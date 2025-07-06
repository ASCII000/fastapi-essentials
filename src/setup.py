# pylint: disable=invalid-name, too-few-public-methods

"""
Modulo de a estrutura de inicializacao da aplicacao
"""

from typing import TypeVar, Type
import logging

from dotenv import dotenv_values


T = TypeVar("T")

class Setup:
    """
    Classe que contem a estrutura de configuração da aplicação.
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

    def get_env(
        self,
        value: str,
        default_value: str = None,
        type_value: Type[T] = str,
    ) -> T:
        """
        Obtem o valor de uma variavel de ambiente

        Arg:
            value: chave da variavel de ambiente
            default_value: valor padrao da variavel de ambiente
            type_value: tipo da variavel de ambiente
        
        Return:
            Valor da variavel de ambiente
        """

        try:

            # Tenta converter o valor da variavel de ambiente
            result = self.env.get(value, default_value)
            return type_value(result) if result is not None else default_value

        except ValueError as err:

            # Se nao conseguir converter o valor da variavel de ambiente
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

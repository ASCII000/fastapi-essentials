"""
Factory for manager authentication
"""

from .auth_interfaces import (
    AuthenticationFactoryInterface,
    BaseLoginInputStrategy,
    LoginStrategies,
)

from .auth_models import JWTToken


class AuthenticationFactory(AuthenticationFactoryInterface):
    """
    Factory for manager authentication
    """

    async def login(self, input_strategy: BaseLoginInputStrategy) -> JWTToken:

        match input_strategy.__strategy__:

            case LoginStrategies.EMAIL_PASSWORD.value:

                # Login with password
                employee = await input_strategy.login()

                # Generate tokens
                payload = {
                    "nome": employee.nome,
                    "email": employee.email,
                }

                access_token = self.jwt_manager.encode(payload, 15)
                refresh_token = self.jwt_manager.encode(payload, 60)

                return JWTToken(
                    access_token=access_token,
                    refresh_token=refresh_token
                )

            case LoginStrategies.GOOGLE.value:
                raise NotImplementedError("Google login not implemented")

            case LoginStrategies.DISCORD.value:
                raise NotImplementedError("Discord login not implemented")

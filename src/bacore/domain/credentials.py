"""Credential domain model."""
from pydantic import BaseModel, SecretStr


class Secret(BaseModel):
    """Secret class which contains secret related settings.

    Attributes:
        secret: The secret.
    """

    secret: SecretStr

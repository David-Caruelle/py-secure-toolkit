import secrets
import string


class SecretGenerator:
    """Generate cryptographically secure application secrets."""

    DEFAULT_ALPHABET = (
        string.ascii_letters
        + string.digits
        + "-_"
    )

    @staticmethod
    def generate(
        length: int = 64,
        alphabet: str | None = None,
    ) -> str:
        """
        Generate a secure random secret.

        Args:
            length: Number of characters.
            alphabet: Optional custom character set.

        Returns:
            A cryptographically secure random string.
        """

        if length < 16:
            raise ValueError(
                "Secret length must be at least 16 characters."
            )

        characters = alphabet or SecretGenerator.DEFAULT_ALPHABET

        if not characters:
            raise ValueError(
                "Alphabet cannot be empty."
            )

        return "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

    @staticmethod
    def hex(bytes_length: int = 32) -> str:
        """
        Generate a hexadecimal secret.

        32 bytes = 64 hexadecimal characters.
        """

        if bytes_length < 16:
            raise ValueError(
                "Secret must contain at least 16 bytes."
            )

        return secrets.token_hex(bytes_length)

    @staticmethod
    def urlsafe(bytes_length: int = 32) -> str:
        """
        Generate a URL-safe secret.
        """

        if bytes_length < 16:
            raise ValueError(
                "Secret must contain at least 16 bytes."
            )

        return secrets.token_urlsafe(bytes_length)

    @staticmethod
    def env(
        name: str = "APP_SECRET",
        bytes_length: int = 32,
    ) -> str:
        """
        Generate a .env-compatible variable.

        Example:
            APP_SECRET=xxxxxxxxxxxxxxxx
        """

        if not name:
            raise ValueError(
                "Environment variable name cannot be empty."
            )

        value = SecretGenerator.urlsafe(bytes_length)

        return f"{name}={value}"

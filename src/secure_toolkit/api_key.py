from .token import TokenGenerator


class ApiKeyGenerator:

    @staticmethod
    def generate(
        prefix: str = "sk",
        bytes_length: int = 32,
    ) -> str:

        token = TokenGenerator.base64_url(bytes_length)

        if not prefix:
            return token

        return f"{prefix}_{token}"

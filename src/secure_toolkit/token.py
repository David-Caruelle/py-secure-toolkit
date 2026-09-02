import secrets
import base64


class TokenGenerator:

    @staticmethod
    def hex(bytes_length: int = 32) -> str:
        if bytes_length < 1:
            raise ValueError("bytes_length must be greater than 0.")

        return secrets.token_hex(bytes_length)

    @staticmethod
    def base64_url(bytes_length: int = 32) -> str:
        if bytes_length < 1:
            raise ValueError("bytes_length must be greater than 0.")

        token = secrets.token_bytes(bytes_length)

        return base64.urlsafe_b64encode(token).decode().rstrip("=")

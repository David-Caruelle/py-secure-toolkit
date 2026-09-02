from pathlib import Path

from .secret import SecretGenerator


DEFAULT_VARIABLES = [
    "APP_SECRET",
    "JWT_SECRET",
    "SESSION_SECRET",
    "API_SECRET",
]


class EnvGenerator:
    """Generate secure environment variables."""

    @staticmethod
    def generate(count: int = 4) -> str:
        """
        Generate environment variables.

        Args:
            count: Number of variables to generate.

        Returns:
            A string containing .env-compatible variables.
        """

        if count < 1:
            raise ValueError("Count must be at least 1.")

        lines = []

        for index in range(count):
            if index < len(DEFAULT_VARIABLES):
                name = DEFAULT_VARIABLES[index]
            else:
                name = f"SECRET_{index + 1}"

            value = SecretGenerator.urlsafe(32)

            lines.append(f"{name}={value}")

        return "\n".join(lines)

    @staticmethod
    def write(
        filename: str = ".env",
        count: int = 4,
    ) -> Path:
        """
        Generate secrets and write them to a .env file.
        """

        content = EnvGenerator.generate(count)

        path = Path(filename)

        path.write_text(
            content + "\n",
            encoding="utf-8",
        )

        return path

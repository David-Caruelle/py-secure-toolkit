import secrets
import string


class PasswordGenerator:

    @staticmethod
    def generate(
        length: int = 20,
        lowercase: bool = True,
        uppercase: bool = True,
        numbers: bool = True,
        symbols: bool = True,
    ) -> str:

        if length < 4:
            raise ValueError("Password length must be at least 4.")

        sets = []

        if lowercase:
            sets.append(string.ascii_lowercase)

        if uppercase:
            sets.append(string.ascii_uppercase)

        if numbers:
            sets.append(string.digits)

        if symbols:
            sets.append("!@#$%^&*()-_=+[]{}?")

        if not sets:
            raise ValueError(
                "At least one character set must be enabled."
            )

        if length < len(sets):
            raise ValueError(
                "Password length is too short."
            )

        password = [
            secrets.choice(characters)
            for characters in sets
        ]

        alphabet = "".join(sets)

        password.extend(
            secrets.choice(alphabet)
            for _ in range(length - len(password))
        )

        secrets.SystemRandom().shuffle(password)

        return "".join(password)

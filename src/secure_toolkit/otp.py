import secrets


class OtpGenerator:

    @staticmethod
    def numeric(length: int = 6) -> str:

        if length < 4 or length > 12:
            raise ValueError(
                "OTP length must be between 4 and 12."
            )

        return "".join(
            str(secrets.randbelow(10))
            for _ in range(length)
        )

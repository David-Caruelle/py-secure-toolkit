from secure_toolkit import (
    ApiKeyGenerator,
    OtpGenerator,
    PasswordGenerator,
    SecretGenerator,
    TokenGenerator,
    UuidGenerator,
)


def main() -> None:
    print("=" * 50)
    print("PHP/Python Secure Toolkit - Python Example")
    print("=" * 50)

    # --------------------------------------------------
    # Password
    # --------------------------------------------------

    password = PasswordGenerator.generate(
        length=24,
        lowercase=True,
        uppercase=True,
        numbers=True,
        symbols=True,
    )

    print("\nPassword:")
    print(password)

    # --------------------------------------------------
    # Hexadecimal token
    # --------------------------------------------------

    hex_token = TokenGenerator.hex(32)

    print("\nHex token:")
    print(hex_token)

    # --------------------------------------------------
    # URL-safe token
    # --------------------------------------------------

    url_token = TokenGenerator.base64_url(32)

    print("\nURL-safe token:")
    print(url_token)

    # --------------------------------------------------
    # API key
    # --------------------------------------------------

    api_key = ApiKeyGenerator.generate(
        prefix="sk",
        bytes_length=32,
    )

    print("\nAPI key:")
    print(api_key)

    # --------------------------------------------------
    # OTP
    # --------------------------------------------------

    otp = OtpGenerator.numeric(6)

    print("\nOTP:")
    print(otp)

    # --------------------------------------------------
    # Application secret
    # --------------------------------------------------

    secret = SecretGenerator.generate(64)

    print("\nApplication secret:")
    print(secret)

    # --------------------------------------------------
    # Hexadecimal secret
    # --------------------------------------------------

    hex_secret = SecretGenerator.hex(32)

    print("\nHex secret:")
    print(hex_secret)

    # --------------------------------------------------
    # URL-safe secret
    # --------------------------------------------------

    url_secret = SecretGenerator.urlsafe(32)

    print("\nURL-safe secret:")
    print(url_secret)

    # --------------------------------------------------
    # .env variable
    # --------------------------------------------------

    env_secret = SecretGenerator.env(
        name="APP_SECRET",
        bytes_length=32,
    )

    print("\n.env variable:")
    print(env_secret)

    # --------------------------------------------------
    # UUID v4
    # --------------------------------------------------

    uuid = UuidGenerator.v4()

    print("\nUUID v4:")
    print(uuid)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()

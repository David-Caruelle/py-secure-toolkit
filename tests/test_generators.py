import re

import pytest

from secure_toolkit import (
    ApiKeyGenerator,
    OtpGenerator,
    PasswordGenerator,
    SecretGenerator,
    TokenGenerator,
    UuidGenerator,
)


# ============================================================
# PasswordGenerator
# ============================================================

def test_password_default_length():
    password = PasswordGenerator.generate()

    assert len(password) == 20


def test_password_custom_length():
    password = PasswordGenerator.generate(32)

    assert len(password) == 32


def test_password_contains_lowercase():
    password = PasswordGenerator.generate(
        length=32,
        lowercase=True,
        uppercase=False,
        numbers=False,
        symbols=False,
    )

    assert password.islower()
    assert password.isalpha()


def test_password_contains_numbers():
    password = PasswordGenerator.generate(
        length=32,
        lowercase=False,
        uppercase=False,
        numbers=True,
        symbols=False,
    )

    assert password.isdigit()


def test_password_contains_all_character_types():
    password = PasswordGenerator.generate(
        length=64,
        lowercase=True,
        uppercase=True,
        numbers=True,
        symbols=True,
    )

    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)

    symbols = "!@#$%^&*()-_=+[]{}?"

    assert any(c in symbols for c in password)


def test_passwords_are_different():
    password1 = PasswordGenerator.generate(32)
    password2 = PasswordGenerator.generate(32)

    assert password1 != password2


def test_password_too_short():
    with pytest.raises(ValueError):
        PasswordGenerator.generate(3)


def test_password_without_character_sets():
    with pytest.raises(ValueError):
        PasswordGenerator.generate(
            20,
            lowercase=False,
            uppercase=False,
            numbers=False,
            symbols=False,
        )


# ============================================================
# TokenGenerator
# ============================================================

def test_hex_token():
    token = TokenGenerator.hex(32)

    assert len(token) == 64
    assert re.fullmatch(r"[0-9a-f]+", token)


def test_hex_tokens_are_different():
    token1 = TokenGenerator.hex(32)
    token2 = TokenGenerator.hex(32)

    assert token1 != token2


def test_base64_url_token():
    token = TokenGenerator.base64_url(32)

    assert len(token) > 0
    assert re.fullmatch(r"[A-Za-z0-9_-]+", token)


def test_hex_token_invalid_length():
    with pytest.raises(ValueError):
        TokenGenerator.hex(0)


def test_base64_token_invalid_length():
    with pytest.raises(ValueError):
        TokenGenerator.base64_url(0)


# ============================================================
# ApiKeyGenerator
# ============================================================

def test_api_key_prefix():
    api_key = ApiKeyGenerator.generate(
        prefix="sk",
        bytes_length=32,
    )

    assert api_key.startswith("sk_")


def test_api_key_custom_prefix():
    api_key = ApiKeyGenerator.generate(
        prefix="production",
        bytes_length=32,
    )

    assert api_key.startswith("production_")


def test_api_key_without_prefix():
    api_key = ApiKeyGenerator.generate(
        prefix="",
        bytes_length=32,
    )

    assert len(api_key) > 0
    assert not api_key.startswith("_")


def test_api_keys_are_different():
    key1 = ApiKeyGenerator.generate()
    key2 = ApiKeyGenerator.generate()

    assert key1 != key2


# ============================================================
# OtpGenerator
# ============================================================

def test_otp_default():
    otp = OtpGenerator.numeric()

    assert len(otp) == 6
    assert otp.isdigit()


def test_otp_custom_length():
    otp = OtpGenerator.numeric(8)

    assert len(otp) == 8
    assert otp.isdigit()


def test_otp_too_short():
    with pytest.raises(ValueError):
        OtpGenerator.numeric(3)


def test_otp_too_long():
    with pytest.raises(ValueError):
        OtpGenerator.numeric(13)


# ============================================================
# SecretGenerator
# ============================================================

def test_secret():
    secret = SecretGenerator.generate(32)

    assert len(secret) == 32


def test_secret_custom_alphabet():
    secret = SecretGenerator.generate(
        length=32,
        alphabet="ABC123",
    )

    assert len(secret) == 32
    assert all(c in "ABC123" for c in secret)


def test_secret_too_short():
    with pytest.raises(ValueError):
        SecretGenerator.generate(15)


def test_hex_secret():
    secret = SecretGenerator.hex(32)

    assert len(secret) == 64
    assert re.fullmatch(r"[0-9a-f]+", secret)


def test_urlsafe_secret():
    secret = SecretGenerator.urlsafe(32)

    assert len(secret) > 0
    assert re.fullmatch(r"[A-Za-z0-9_-]+", secret)


def test_env_secret():
    env = SecretGenerator.env(
        name="APP_SECRET",
        bytes_length=32,
    )

    assert env.startswith("APP_SECRET=")

    name, value = env.split("=", 1)

    assert name == "APP_SECRET"
    assert len(value) > 0


def test_empty_env_name():
    with pytest.raises(ValueError):
        SecretGenerator.env(
            name="",
            bytes_length=32,
        )


# ============================================================
# UuidGenerator
# ============================================================

def test_uuid_v4():
    uuid = UuidGenerator.v4()

    pattern = (
        r"^[0-9a-f]{8}-"
        r"[0-9a-f]{4}-"
        r"4[0-9a-f]{3}-"
        r"[89ab][0-9a-f]{3}-"
        r"[0-9a-f]{12}$"
    )

    assert re.fullmatch(pattern, uuid)


def test_uuid_is_unique():
    uuid1 = UuidGenerator.v4()
    uuid2 = UuidGenerator.v4()

    assert uuid1 != uuid2

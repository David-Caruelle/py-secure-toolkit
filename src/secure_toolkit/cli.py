import argparse

from .api_key import ApiKeyGenerator
from .otp import OtpGenerator
from .password import PasswordGenerator
from .secret import SecretGenerator
from .token import TokenGenerator
from .uuid import UuidGenerator
from .env import EnvGenerator


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="secure",
        description="Secure Toolkit - Security generators for developers",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # ---------------------------------------------------------
    # password
    # ---------------------------------------------------------

    password_parser = subparsers.add_parser(
        "password",
        help="Generate a secure password",
    )

    password_parser.add_argument(
        "--length",
        type=int,
        default=20,
        help="Password length (default: 20)",
    )

    password_parser.add_argument(
        "--no-lowercase",
        action="store_true",
        help="Disable lowercase characters",
    )

    password_parser.add_argument(
        "--no-uppercase",
        action="store_true",
        help="Disable uppercase characters",
    )

    password_parser.add_argument(
        "--no-numbers",
        action="store_true",
        help="Disable numbers",
    )

    password_parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Disable symbols",
    )

    # ---------------------------------------------------------
    # token
    # ---------------------------------------------------------

    token_parser = subparsers.add_parser(
        "token",
        help="Generate a secure token",
    )

    token_parser.add_argument(
        "--type",
        choices=["hex", "url"],
        default="hex",
        help="Token type",
    )

    token_parser.add_argument(
        "--bytes",
        type=int,
        default=32,
        help="Number of random bytes",
    )

    # ---------------------------------------------------------
    # api-key
    # ---------------------------------------------------------

    api_parser = subparsers.add_parser(
        "api-key",
        help="Generate an API key",
    )

    api_parser.add_argument(
        "--prefix",
        default="sk",
        help="API key prefix",
    )

    api_parser.add_argument(
        "--bytes",
        type=int,
        default=32,
        help="Number of random bytes",
    )

    # ---------------------------------------------------------
    # otp
    # ---------------------------------------------------------

    otp_parser = subparsers.add_parser(
        "otp",
        help="Generate a numeric OTP",
    )

    otp_parser.add_argument(
        "--length",
        type=int,
        default=6,
        help="OTP length",
    )

    # ---------------------------------------------------------
    # secret
    # ---------------------------------------------------------

    secret_parser = subparsers.add_parser(
        "secret",
        help="Generate an application secret",
    )

    secret_parser.add_argument(
        "--length",
        type=int,
        default=64,
        help="Secret length",
    )

    # ---------------------------------------------------------
    # uuid
    # ---------------------------------------------------------

    subparsers.add_parser(
        "uuid",
        help="Generate a UUID v4",
    )

    # ---------------------------------------------------------
    # env
    # ---------------------------------------------------------

    env_parser = subparsers.add_parser(
        "env",
        help="Generate secure .env variables",
    )

    env_parser.add_argument(
        "--count",
        type=int,
        default=4,
        help="Number of secrets to generate",
    )

    env_parser.add_argument(
        "--output",
        default=None,
        help="Write variables to a .env file",
    )

    args = parser.parse_args()

    # ---------------------------------------------------------
    # Execute command
    # ---------------------------------------------------------

    try:
        if args.command == "password":
            result = PasswordGenerator.generate(
                length=args.length,
                lowercase=not args.no_lowercase,
                uppercase=not args.no_uppercase,
                numbers=not args.no_numbers,
                symbols=not args.no_symbols,
            )

        elif args.command == "token":
            if args.type == "hex":
                result = TokenGenerator.hex(args.bytes)
            else:
                result = TokenGenerator.base64_url(args.bytes)

        elif args.command == "api-key":
            result = ApiKeyGenerator.generate(
                prefix=args.prefix,
                bytes_length=args.bytes,
            )

        elif args.command == "otp":
            result = OtpGenerator.numeric(args.length)

        elif args.command == "secret":
            result = SecretGenerator.generate(args.length)

        elif args.command == "uuid":
            result = UuidGenerator.v4()

        elif args.command == "env":
            if args.output:
                path = EnvGenerator.write(
                    filename=args.output,
                    count=args.count,
                )

                print(f"Environment file created: {path}")
                return

            result = EnvGenerator.generate(args.count)

        else:
            parser.error("Unknown command.")

        print(result)

    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()

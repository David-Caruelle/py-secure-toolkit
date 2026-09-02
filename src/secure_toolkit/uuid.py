import uuid


class UuidGenerator:

    @staticmethod
    def v4() -> str:
        return str(uuid.uuid4())

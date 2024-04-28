class NotFoundApiException(Exception):
    def __init__(self, name: str, *args: object):
        self.msg = name
        super().__init__(*args)

class MissingArgumentException(Exception):
    def __init__(self, message: str, arguments: list[str], *args: object) -> None:
        self.message = message
        self.arguments = arguments
        super().__init__(*args)

class UnauthorizedApiException(Exception):
    def __init__(self, name: str, *args: object):
        self.name = name
        super().__init__(*args)

class NotImplementedException(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(*args)

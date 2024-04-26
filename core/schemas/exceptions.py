class MissingArumentException(Exception):
    def __init__(self, message: str, arguments: list[str], *args: object) -> None:
        self.message = message
        self.arguments = arguments
        super().__init__(*args)
from core.schemas.exceptions import *

api_responses = {
    404: {
        "description": "Item not found",
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/NotFoundApiError"
                    }
                }
            }
        },
    520: {
        "description": "Missing arguments",
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/MissingArgumetsError"
                    }
                }
            }
        },
}

class NotFoundApiException(Exception):
    def __init__(self, name: str, *args: object):
        self.msg = name
        super().__init__(*args)

class UnauthorizedApiException(Exception):
    def __init__(self, name: str, *args: object):
        self.name = name
        super().__init__(*args)
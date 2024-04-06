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
}

class NotFoundApiException(Exception):
    def __init__(self, name: str):
        self.msg = name

class UnauthorizedApiException(Exception):
    def __init__(self, name: str):
        self.name = name
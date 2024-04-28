import types
from typing import Callable
from urllib import response
from core.schemas import ALL_SCHEMA_CLASSES
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
    401: {
        "description": "Not authorized",
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/UnauthorizedApiError"
                }
            }
        }
    },
}

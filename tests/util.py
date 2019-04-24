from unittest.mock import patch

from spoffy.client import Client


def mock_get(response):
    def decorator(func):
        return patch.object(Client, "get", return_value=response)(func)

    return decorator


def mock_put(response):
    def decorator(func):
        return patch.object(Client, "put", return_value=response)(func)

    return decorator


def mock_delete(response):
    def decorator(func):
        return patch.object(Client, "delete", return_value=response)(func)

    return decorator

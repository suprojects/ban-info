"""Errors returned by the API"""
from datetime import datetime

from requests import Response

from .types import Token


class OwlAntiSpamError(Exception):
    pass


class Error(OwlAntiSpamError):
    def __init__(self, req: Response) -> None:
        self.status_code = req.status_code
        self.text = req.text
        self.url = req.url
        Exception.__init__(self, f'code: {self.status_code} body: `{self.text}` url: {self.url}')


class UnauthorizedError(OwlAntiSpamError):
    pass


class NotFoundError(OwlAntiSpamError):
    pass


class Forbidden(OwlAntiSpamError):
    def __init__(self, token: Token) -> None:
        Exception.__init__(self, f"Your tokens permission `{token.permission}` is not high enough.")


class TooManyRequests(OwlAntiSpamError):
    until: datetime
    method: str

    def __init__(self, method, until: int) -> None:
        self.method = method
        self.until = datetime.fromtimestamp(until)
        Exception.__init__(self, f"Too Many Requests for method `{method}`. Try again in {self.until - datetime.now()}")

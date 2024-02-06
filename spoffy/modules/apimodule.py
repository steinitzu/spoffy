from abc import abstractmethod
from typing import TypeVar, Awaitable, Any
import time

from spoffy.sansio import Request
from spoffy.client.base import AsyncClient, SyncClient


TLoaded = TypeVar("TLoaded")


class AsyncApiModule:
    def __init__(self, client: AsyncClient):
        self.client = client
        self.b = self.__builder_class__(client)

    async def _make_request(self, req: Request, target):
        return self.client.load(await self.client.request(req), target)

    async def _assign_token(self, response: Awaitable):
        token = await response
        token["expires_at"] = int(time.time() + token["expires_in"])
        self.client.token = token

    @property
    @abstractmethod
    def __builder_class__(self):
        pass


class ApiModule:
    def __init__(self, client: SyncClient):
        self.client = client
        self.b = self.__builder_class__(client)

    def _make_request(self, req: Request, target):
        return self.client.load(self.client.request(req), target)

    def _assign_token(self, response: Any):
        token = response
        token["expires_at"] = int(time.time() + token["expires_in"])
        self.client.token = token

    @property
    @abstractmethod
    def __builder_class__(self):
        pass

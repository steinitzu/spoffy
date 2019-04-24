from abc import abstractmethod


from spoffy.client.common import ClientCommon
from spoffy.sansio import Response
from spoffy.sansio import Request


class AsyncClient(ClientCommon):
    """
    Base class for async spotify client.
    Subclasses must implement the :meth:`~AsyncClient.request` method
    """

    @abstractmethod
    async def request(self, request: Request) -> Response:
        pass


class SyncClient(ClientCommon):
    """
    Base class for a sync spotify client.
    Subclasses must implement the :meth:`~SyncClient.request` method
    """

    @abstractmethod
    def request(self, request: Request) -> Response:
        pass


SyncClient.__doc__ += ClientCommon.__doc__.split("----")[1]  # type: ignore
AsyncClient.__doc__ += ClientCommon.__doc__.split("----")[1]  # type: ignore

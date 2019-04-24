from typing import Optional

import aiohttp

from spoffy.models import Token
from spoffy.client.base import AsyncClient, ClientCommon
from spoffy.sansio import Request, Response
from spoffy.spotify import AsyncSpotify


class AioHttpClient(AsyncClient):
    """
    Client implementation using requests as a http backend

    :param session: A :class:`~aiohttp.ClientSession` object
    """

    def __init__(
        self,
        *,
        session: aiohttp.ClientSession,
        access_token: Optional[str] = None,
        token: Optional[Token] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:

        self.session = session
        super().__init__(
            access_token,
            token,
            client_id,
            client_secret,
            redirect_uri,
            scope,
            state,
        )

    async def request(self, request: Request) -> Response:
        async with self.session.request(
            method=request.method,
            url=request.url,
            data=request.body,
            headers=request.headers,
        ) as resp:
            response = Response(
                request, resp.status, resp.headers, await resp.read()
            )
            response.raise_for_status()
            return response


def make_spotify(
    *,
    session: aiohttp.ClientSession,
    access_token: Optional[str] = None,
    token: Optional[Token] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    redirect_uri: Optional[str] = None,
    scope: Optional[str] = None,
    state: Optional[str] = None,
) -> AsyncSpotify:
    """
    Convenience factory to build
    Spotify API wrapper using the requests http library.
    Accepts all arguments of :class:`~AioHttpClient`
    """
    return AsyncSpotify(
        AioHttpClient(
            session=session,
            access_token=access_token,
            token=token,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            state=state,
        )
    )


AioHttpClient.__doc__ += ClientCommon.__doc__.split("----")[1]  # type: ignore
make_spotify.__doc__ += ClientCommon.__doc__.split("----")[1]  # type: ignore

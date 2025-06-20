from typing import Optional

import httpx

from spoffy.models import Token
from spoffy.client.base import AsyncClient, ClientCommon
from spoffy.sansio import Request, Response
from spoffy.spotify import AsyncSpotify


class AsyncHttpXClient(AsyncClient):
    """
    Client implementation using httpx as a http backend

    :param session: A :class:`~requests.Session` object
    """

    def __init__(
        self,
        *,
        session: Optional[httpx.AsyncClient] = None,
        access_token: Optional[str] = None,
        token: Optional[Token] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        self.session: httpx.AsyncClient = session or httpx.AsyncClient()  # type: ignore
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
        resp = await self.session.request(
            method=request.method,
            url=request.url,
            content=request.body,
            headers=request.headers,
        )
        response = Response(request, resp.status_code, resp.headers, resp.content)
        response.raise_for_status()
        return response


def make_spotify(
    *,
    session: Optional[httpx.AsyncClient] = None,
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
    Accepts all arguments of :class:`~HttpXClient`
    """
    return AsyncSpotify(
        AsyncHttpXClient(
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


AsyncHttpXClient.__doc__ += ClientCommon.__doc__.split("----")[1]  # type: ignore
make_spotify.__doc__ += ClientCommon.__doc__.split("----")[1]  # type: ignore

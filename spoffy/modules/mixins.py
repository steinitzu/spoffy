from urlobject import URLObject


class AuthMixin:
    def get_authorize_url(self, **kwargs) -> str:
        params = dict(
            client_id=self.client.client_id,  # type: ignore
            redirect_uri=self.client.redirect_uri,  # type: ignore
            scope=self.client.scope,  # type: ignore
            state=self.client.state,  # type: ignore
            response_type="code",
        )
        params.update(kwargs)
        return str(
            URLObject(
                self.client.authorize_url  # type: ignore
            ).add_query_params(**params)
        )

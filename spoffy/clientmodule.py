from spoffy.oldclient import Client


class ClientModule:
    """
    A base client module

    :param client: A `Client` instance
    """

    def __init__(self, client: Client) -> None:
        self.client = client

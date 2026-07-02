from .generated.client import Pipe2GraphQLClient


class Pipe2Client(Pipe2GraphQLClient):
    """Pipe2.ai Python SDK client.

    Usage:
        client = Pipe2Client(token="eyJ...")
        pipelines = await client.get_pipelines()
    """

    def __init__(
        self,
        token: str,
        endpoint: str = "https://api.pipe2.ai/v1/graphql",
    ):
        super().__init__(
            url=endpoint,
            headers={"Authorization": f"Bearer {token}"},
        )

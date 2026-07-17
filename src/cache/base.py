import abc
import typing


class AccessCache(abc.ABC):
    def __init__(self, ctx, prefix=None, cache_ttl=0, continuation=None, **kwargs):
        self.ctx = ctx
        self.continuation = continuation
        self.kwargs = kwargs

    @abc.abstractmethod
    def fetch(self) -> typing.Dict[str, typing.Any]:
        """Fetches results from Tumblr"""
        pass

    @abc.abstractmethod
    def parse(self, initial_results):
        """Parses the initial JSON response from Tumblr"""
        pass

    async def get(self):
        """Retrieves some data from Tumblr itself"""
        initial_results = await self.fetch()
        return self.parse(initial_results)

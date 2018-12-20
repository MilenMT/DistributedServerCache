class Data:

    """
    Stores all data needed for our simulation

    endpoints: list<Endpoint>
    videos_sizes: list<int>
    number_of_cache_servers: int
    requests: list<Requestinfo>
    cache_size: int
    """

    def __init__(self, endpoints, videos_sizes, number_of_cache_servers, requests, cache_size):
        self.endpoints = endpoints
        self.videos_sizes = videos_sizes
        self.amount_of_cache_servers = number_of_cache_servers
        self.requests = requests
        self.cache_size = cache_size

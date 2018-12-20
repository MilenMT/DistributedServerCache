class RequestInfo:
    def __init__(self, video_id, endpoint_id, amount_of_requests):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.amount_of_requests = amount_of_requests

    def __str__(self):
        return self.__pretty_string_representation()

    def __pretty_string_representation(self):
        return "{0} requests for video {1} coming from endpoint {2}"\
            .format(self.amount_of_requests, self.video_id, self.endpoint_id)

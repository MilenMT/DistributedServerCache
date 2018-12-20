from parsers.solution_parser import parse_solution
from parsers.input_parser import parse_input
from datarepresentation.endpoint import Endpoint
from datarepresentation.data import Data


def check_solution(path_to_input_file: str, path_to_solution_file: str):
    """
    Check whether solution is valid or not and if it is valid calculate solution score.

    :param path_to_input_file: path to input file as string
    :param path_to_solution_file: path to solution file as string
    :return: solution score (int)
    """
    input_data = parse_input(path_to_input_file)
    solution = parse_solution(path_to_solution_file)
    validation_result = __validate_solution(input_data, solution)
    if validation_result is True:
        return calculate_score(input_data, solution)
    raise Exception("Solution is not valid! (total size of "
                    "videos stored at server #{0} exceeds "
                    "server capacity)".format(validation_result))


def __validate_solution(input_data: Data, solution: dict):
    """
    Checks whether solution is valid or not.

    :param input_data: tuple of input data
    :param solution: dictionary of solution data
    :return: returns True if solution is valid. if solution
             is not valid returns index of invalid server.
    """
    server_capacity = input_data.cache_size
    videos_sizes = input_data.videos_sizes
    for server_id in sorted(solution.keys()):
        server_content_size = 0
        for video_id in solution[server_id]:
            server_content_size += videos_sizes[video_id]
        if server_content_size > server_capacity:
            return server_id
    return True


def calculate_score(input_data: Data, solution: dict):
    """
    Calculates solution score - average time saved in microseconds.

    :param input_data: tuple of input data
    :param solution: dictionary of solution data
    :return: average time saved in microseconds (int)
    """
    total_time_saved = 0
    total_requests = 0
    requests = input_data.requests
    endpoints = input_data.endpoints
    for request in requests:
        video_id = request.video_id
        endpoint = endpoints[request.endpoint_id]
        time_saved_per_request = __calculate_time_saved_per_request(endpoint, solution, video_id)
        total_time_saved += time_saved_per_request * request.amount_of_requests
        total_requests += request.amount_of_requests
    average_time_saved = total_time_saved / total_requests
    return average_time_saved * 1000


def __calculate_time_saved_per_request(endpoint: Endpoint, solution: dict, video_id: int):
    lowest_latency = endpoint.datacenter_latency
    for server_id in endpoint.cache_server_latencies.keys():
        if video_id in solution[server_id]:
            latency_to_cache = endpoint.cache_server_latencies[server_id]
            if lowest_latency > latency_to_cache:
                lowest_latency = latency_to_cache
    return endpoint.datacenter_latency - lowest_latency

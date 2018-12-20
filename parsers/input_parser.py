from datarepresentation.endpoint import Endpoint
from datarepresentation.requestinfo import RequestInfo
from datarepresentation.data import Data


def parse_input(path_to_file: str):
    """
    Parses input file.

    :param path_to_file: path to input file as string
    :return: Data objet containing a complete description of input (see datarepresentation/data.py)
    """
    amount_of_videos, amount_of_endpoints, amount_of_request_descriptions, \
        amount_of_cache_servers, cache_size = -1, -1, -1, -1, -1
    videos_sizes = dict()
    endpoints = dict()
    requests = list()
    if not path_to_file.endswith(".in"):
        raise Exception("Invalid input file extension.")
    with open(path_to_file) as file:
        line_number = 0
        next_endpoint_definition_at_line = 3
        endpoint_id = 0
        current_endpoint = None
        for line in file:
            line_content = line.strip().split(" ")
            line_number += 1
            if line_number == 1:
                amount_of_videos, amount_of_endpoints, amount_of_request_descriptions,\
                    amount_of_cache_servers, cache_size = __parse_general_data(line_content)
            elif line_number == 2:
                videos_sizes = __parse_video_sizes(line_content)
            else:
                line_size = len(line_content)
                if line_size == 2:
                    if line_number == next_endpoint_definition_at_line:
                        current_endpoint = __parse_endpoint_definition(endpoint_id, line_content)
                        endpoints[endpoint_id] = current_endpoint
                        next_endpoint_definition_at_line = __calculate_line_of_next_endpoint(line_number,
                                                                                             current_endpoint)
                        endpoint_id += 1
                    else:
                        cache_id, latency = __parse_latency_to_cache_server(line_content)
                        current_endpoint.cache_server_latencies[cache_id] = latency
                elif line_size == 3:
                    requests.append(__parse_request_info(line_content))
                else:
                    raise Exception("Incorrect input at line {0}.".format(line_number))

    return Data(endpoints, videos_sizes, amount_of_cache_servers, requests, cache_size)


def __parse_general_data(line_content: list):
    return tuple(int(x) for x in line_content)


def __parse_video_sizes(line_content: list):
    video_sizes = dict()
    video_sizes_list = line_content
    for i in range(0, len(video_sizes_list)):
        video_sizes[i] = int(video_sizes_list[i])
    return video_sizes


def __parse_endpoint_definition(id_: int, line_content: list):
    endpoint_parameters = tuple(int(x) for x in line_content)
    return Endpoint(id_, endpoint_parameters[0], endpoint_parameters[1])


def __calculate_line_of_next_endpoint(line_number: int, current_endpoint: Endpoint):
    return line_number + current_endpoint.amount_of_caches + 1


def __parse_latency_to_cache_server(line_content: list):
    return tuple(int(x) for x in line_content)


def __parse_request_info(line_content: list):
    request_information = tuple(int(x) for x in line_content)
    return RequestInfo(request_information[0], request_information[1], request_information[2])

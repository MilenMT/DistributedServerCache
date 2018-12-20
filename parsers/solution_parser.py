def parse_solution(path_to_file: str):
    """
    Parses solution file.

    :param path_to_file: path to solution file as string
    :return: dictionary consisting of pairs:
             server_id (int), list of video ids (as ints)
    """
    solution = dict()
    if not path_to_file.endswith(".out"):
        raise Exception("Invalid solution file extension.")
    with open(path_to_file) as file:
        line_number, amount_of_servers = -1, -1
        for line in file:
            line_number += 1
            if line_number == 0:
                amount_of_servers = int(line)
            elif line_number > amount_of_servers:
                print("Too many lines. Skipping lines from {0} onwards."
                      .format(line_number))
                break
            else:
                line = line.strip().split(" ")
                server_id = __parse_server_id(line)
                videos_ids = __parse_video_ids(line)
                solution[server_id] = videos_ids
    return solution


def __parse_server_id(line: list):
    return int(line[0])


def __parse_video_ids(line: list):
    return list(int(x) for x in line[1:])

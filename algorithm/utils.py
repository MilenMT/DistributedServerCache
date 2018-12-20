import random
from utils.solution_checker import calculate_score


class AlgorithmUtils:

    @staticmethod
    def random_solution(data):

        res = dict()
        avg_video_size = sum(data.videos_sizes)/len(data.videos_sizes)
        total_n_videos = round(data.cache_size/avg_video_size)

        for s in range(data.amount_of_cache_servers):
            if total_n_videos == 0:
                res[s] = []
            else:
                n_videos = random.randint(0, total_n_videos-1)      # ile filmow losujemy
                res[s] = random.sample(range(len(data.videos_sizes)), n_videos)
                while sum([data.videos_sizes[v] for v in res[s]]) > AlgorithmUtils.free_space(data, res, s):
                    res[s].pop(random.randint(0, len(res[s])-1))

        return res

    @staticmethod
    def random_neighbour(data, solution, radius):

        res = AlgorithmUtils.solution_copy(solution)
        if radius == 0:
            return res

        free_space_on_server = \
            [AlgorithmUtils.free_space(data, solution, s) for s in range(data.amount_of_cache_servers)]

        acceptable_ops = [(s, v)
                          for s in range(data.amount_of_cache_servers)
                          for v in range(len(data.videos_sizes))
                          if v in res[s] or data.videos_sizes[v] <= free_space_on_server[s]]

        op = random.choice(acceptable_ops)
        s = op[0]
        v = op[1]

        if v in res[s]:
            res[s].remove(v)
        else:
            res[s].append(v)

        return AlgorithmUtils.random_neighbour(data, res, radius - 1)

    @staticmethod
    def best_in_neighbourhood(data, solution, radius, number_of_bees):

        neighbours = []
        for _ in range(number_of_bees):
            neighbour = AlgorithmUtils.random_neighbour(data, solution, radius)
            neighbours.append((neighbour, calculate_score(data, neighbour)))
        best_neighbour = max(neighbours, key=lambda s: s[1])
        return best_neighbour[0] if best_neighbour[1] > calculate_score(data, solution) else solution

    @staticmethod
    def free_space(data, solution, server):
        return data.cache_size - sum([data.videos_sizes[v] for v in solution[server]])

    @staticmethod
    def solution_copy(solution):

        res = dict()
        for s in solution:
            res[s] = solution[s][:]
        return res

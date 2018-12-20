from algorithm.utils import AlgorithmUtils
from utils.solution_checker import calculate_score


class Algorithm:
    @staticmethod
    def execute(data, n, m, e, nep, nsp, ngh, iterations):

        pool = [AlgorithmUtils.random_solution(data) for _ in range(n)]
        best_iter = 0
        best_score = 0

        for i in range(iterations):
            solutions_ranking = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
            elite_solutions = solutions_ranking[0:e]
            good_solutions = solutions_ranking[e:m]

            current_best_score = calculate_score(data, solutions_ranking[0])
            if current_best_score > best_score:
                best_score = current_best_score
                best_iter = i

            pool = []
            for es in elite_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, es, ngh, nep))
            for gs in good_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, gs, ngh, nsp))
            for _ in range(n - m):
                pool.append(AlgorithmUtils.random_solution(data))

        pool = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
        return pool[0], best_iter

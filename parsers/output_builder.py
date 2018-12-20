def save_solution(solution, name):
    with open(name, 'w') as f:
        f.write(str(len(solution)) + "\n")
        for s in solution:
            f.write(str(s) + " " + " ".join([str(v) for v in solution[s]]) + "\n")


def save_execution_parameters(separator, file, n, m, e, nep, nsp, ngh, iterations, score, output_file):
    with open(output_file, 'a') as f:
        f.write(separator.join(str(x) for x in (file, n, m, e, nep, nsp, ngh, iterations, score)) + "\n")


def clear_results_file(separator, output_file):
    with open(output_file, 'w') as out:
        out.write(separator.join(("file", "n", "m", "e", "nep", "nsp", "ngh", "iterations", "score")) + "\n")

from argparse import ArgumentParser
from os.path import split
from time import time

from algorithm.algorithm import Algorithm
from parsers.input_parser import parse_input
from parsers.output_builder import save_solution, save_execution_parameters
from utils.argument_parser_util import add_parser_arguments, str2bool
from utils.solution_checker import check_solution, calculate_score


def main():
    input_file, output_file = args.i, args.o
    n, m, e = args.n, args.m, args.e
    nep, nsp, ngh = args.nep, args.nsp, args.ngh
    iterations = args.max
    should_save = str2bool(args.s)

    before = time()
    data = parse_input(input_file)
    alg_res = Algorithm.execute(data, n, m, e, nep, nsp, ngh, iterations)
    best_solution = alg_res[0]
    best_iter = alg_res[1]

    if should_save:
        save_solution(best_solution, output_file)
        score = check_solution(input_file, output_file)
    else:
        score = calculate_score(data, best_solution)
        filename = split(input_file)[1]
        save_execution_parameters(";", filename, n, m, e, nep, nsp, ngh, iterations, score, output_file)
    after = time()

    print(best_solution)
    print("-----------------------------")
    print("Algorithm took: " + str(round(after - before, 2)) + " s")
    print("-----------------------------")
    print("Achieved after iteration: " + str(best_iter+1))
    print("-----------------------------")
    print("Saved time: " + str(round(score / 1000, 2)) + " s (score: " + str(score) + ")")


if __name__ == "__main__":
    parser = ArgumentParser(description="Distributed cache problem solver.")
    add_parser_arguments(parser)
    args = parser.parse_args()
    main()

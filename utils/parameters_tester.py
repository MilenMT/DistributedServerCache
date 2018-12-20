from os.path import join, split
from subprocess import call
from time import time

from concurrent.futures import ProcessPoolExecutor
from os import getcwd

from parsers.output_builder import clear_results_file


def main():
    main_path = __get_path()
    input_dir = join(split(getcwd())[0], "files")
    input_file = join(input_dir, "me_at_the_zoo.in")
    output_dir = join(split(getcwd())[0], "files")
    output_file = join(output_dir, "results.csv")
    clear_results_file(';', output_file)

    bees = 50
    good_solutions = 9
    elite_solutions = 3  # must be lower than good_solutions
    nep = 9
    nsp = 3  # nsp + nep = bees
    ngh = 1
    iterations = 250

    before = time()
    with ProcessPoolExecutor(None) as executor:
        # to run with different parameters add a for loop within "with" block
        # example: "for parameter in range(start, stop, step):"
        nsp = bees - nep
        command = "python {0} -i {1} -o {2} -n {3} -m {4} -e {5} -nep {6} -nsp {7} -ngh {8} -max {9} -s False"\
            .format(main_path, input_file, output_file, bees, good_solutions,
                    elite_solutions, nep, nsp, ngh, iterations)
        executor.submit(call, command)
    after = time()
    print("Execution took: " + str(round(after - before, 2)) + " s")


def __get_path():
    directory = split(getcwd())[0]
    filename = "main.py"
    return join(directory, filename)


if __name__ == '__main__':
    main()

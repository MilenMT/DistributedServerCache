from argparse import ArgumentTypeError
from os.path import join

from os import getcwd


def add_parser_arguments(parser):
    default_input_filename = "me_at_the_zoo.in"
    parser.add_argument("-i", "-input_file", help="Path to input file.", type=str,
                        default=join(getcwd(), "files", default_input_filename))

    default_output_filename = "solution.out"
    parser.add_argument("-o", "-output_file", help="Path to output file.", type=str,
                        default=join(getcwd(), "files", default_output_filename))

    default_n = 25
    parser.add_argument("-n", "-bees", help="Number of bees.", type=int,
                        default=default_n)

    default_m = 9
    parser.add_argument("-m", "-good_solutions", help="Number of good solutions.", type=int,
                        default=default_m)

    default_e = 3
    parser.add_argument("-e", "-elite_solutions", help="Number of elite solutions.", type=int,
                        default=default_e)

    default_nep = 9
    parser.add_argument("-nep", help="Number of solutions searched in elite solutions' neighbourhood", type=int,
                        default=default_nep)

    default_nsp = 3
    parser.add_argument("-nsp", help="Number of solutions searched in good solutions' neighbourhood", type=int,
                        default=default_nsp)

    default_ngh = 1
    parser.add_argument("-ngh", help="Neighborhood radius.", type=int,
                        default=default_ngh)

    default_max_iter = 100
    parser.add_argument("-max", "-iterations", help="Number of iterations.", type=int,
                        default=default_max_iter)

    default_s = "True"
    parser.add_argument("-s", "-save_solution", help="Should solution be saved?", type=str,
                        default=default_s)


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgumentTypeError('Boolean value expected.')

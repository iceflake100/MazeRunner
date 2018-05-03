import argparse
import generator
import solver

def parse_arguments():
    parser = argparse.ArgumentParser()

    # generator arguments
    parser.add_argument("-g", "--generate", default="",
                        help="filename used for generated maze")
    parser.add_argument("-s", "--size", type=int, default=50
                        , help="size NxN of generated maze")

    # solver arguments
    parser.add_argument("-si", "--solve", default=""
                            , help="maze file to solve")
    parser.add_argument("-sg", "--solvegenerated", action="store_true"
                        , default=False, help="generate and then solve a maze")
    parser.add_argument("-dfs", "--dfs", action="store_true"
                        , default=False, help="solve using dfs algorithm")
    parser.add_argument("-dji", "--djikstra", action="store_true"
                        , default=False
                        , help="solve using djikstra algorithm")


    return parser.parse_args()


def main():
    arguments = parse_arguments()

    if arguments.generate:
    generator.create(arguments.generate, arguments.size) 
    if arguments.solvegenerated:
        solver.solve(arguments.generate+".png", arguments.dfs,
                        arguments.djikstra)
    if not arguments.solve == "":
        solver.solve(arguments.solve, arguments.dfs, arguments.djikstra)

if __name__ == "__main__":
    main()

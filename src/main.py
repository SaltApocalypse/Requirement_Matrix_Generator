import sys
import argparse

import excel
import utils
from SheetTree import SheetTree


def cli():
    parser = argparse.ArgumentParser(description="Generate requirement matrix from a textfile (.txt).")
    parser.add_argument("input_file", type=str, help="The path of textfile.")
    parser.add_argument("-o", "--output_path", type=str, help="The path of output (.xlsx file).", default=".")
    parser.add_argument("-n", "--name", type=str, help="Name of the file.", default="requirement_matrix")
    parser.add_argument("-t", "--title", type=str, help="Input the title.", default="MATRIX")

    return parser.parse_args()


def main(args):
    # get args from cli

    # from file get fields  (column comes first)
    files = utils.textLoader(args.input_file)

    column = SheetTree(files[0])  # number
    row = SheetTree(files[1])  # alpha

    # write to .xlsx
    excel.generate_requirement_matrix(column, row, args)


if __name__ == "__main__":
    if sys.gettrace():
        print("Running in IDE or script.")
    else:
        args = cli()
        main(args)

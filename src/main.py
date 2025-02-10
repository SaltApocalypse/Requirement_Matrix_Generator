import sys
import argparse

import utils.excel
import utils.files
from utils.Sheettree import SheetTree


def cli():
    parser = argparse.ArgumentParser(description="Generate requirement matrix from a textfile (.txt).")
    parser.add_argument("-i", "--input_file", type=str, help="The path of textfile.")
    parser.add_argument("-o", "--output_path", type=str, help="The path of output (.xlsx file).", default=".")
    parser.add_argument("-n", "--name", type=str, help="Name of the file.", default="requirement_matrix")
    parser.add_argument("-t", "--title", type=str, help="Input the title.", default="MATRIX")

    return parser.parse_args()


def main(args):
    # from file get fields  (column comes first)
    files = utils.files.textLoader(args.input_file)

    column = SheetTree(files[0])  # number
    row = SheetTree(files[1])  # alpha

    # write to .xlsx
    utils.excel.generate_requirement_matrix(column, row, args)


if __name__ == "__main__":
    args = cli()
    main(args)

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
    # 从文件读取的列标题和行标题
    sections = utils.files.textLoader(args.input_file)

    row = SheetTree(sections[0])  # 行标题
    column = SheetTree(sections[1])  # 列标题

    # 通过文件生成需求矩阵
    utils.excel.generate_requirement_matrix(column, row, output_path=args.output_path, name=args.name, title=args.title)


if __name__ == "__main__":
    args = cli()
    main(args)

from pathlib import Path


def get_file_extension(file: str) -> str:
    """
    返回文件扩展名

    Args:
        - file (str): The name or path of the file.

    Returns:
        - str: The file extension, including the dot.
    """
    return Path(file).suffix


def textLoader(fileName: str) -> list[list[str]]:
    """
    根据扩展名选择加载器。

    Args:
        - fileName (str): 带扩展名的文件名

    Returns:
        - list[list[str]], len = 2: 返回上下两段处理好的内容

    Raises:
        - ValueError: 仅限 .txt 或 .json 文件
    """
    extension = get_file_extension(fileName)
    if ".txt" == extension:
        return textfile_textLoader(fileName)
    raise ValueError("File must have a .txt or .json extension")


def textfile_textLoader(fileName: str) -> list[list[str]]:
    """
    从 .txt 内读取文件然后格式化
    格式化：读取文件，把两段文本分出来

    Args:
        - fileName (str): 文件名

    Returns:
        - list[list[str]]: 分好的两段文字（上下段）
    """
    with open(fileName, "r", encoding="utf-8") as file:
        lines = [[], []]  # 上下段
        pointer = 0
        for line in file:
            line = line.replace("\t", "    ")  # 部分地方导出的文件会有水平制表符

            # 切段
            if pointer < 1 and "" == line.strip():
                pointer += 1

            if line.strip() != "":
                lines[pointer].append(line)

        return lines

    print("Error: Fail to load from textfile.")

import math
from functools import reduce
from pathlib import Path

suppprted_files = [".txt", ".json"]


def gcd_list(numbers: list[int]) -> int:
    """
    Solving for the GCD of a list.

    Args:
        - numbers (list[int]): A list.

    Returns:
        - int: The GCD of the list.
    """
    return reduce(math.gcd, numbers)


def get_file_extension(file: str) -> str:
    """
    Get the file extension from a given file name.

    Args:
        - file (str): The name or path of the file.

    Returns:
        - str: The file extension, including the dot.
    """
    return Path(file).suffix


def number_to_alpha(num: int, offset: int = 0) -> str:
    number = num + offset
    alpha = ""
    while number > 0:
        number -= 1
        alpha = chr(number % 26 + ord("A")) + alpha
        number //= 26
    return alpha


def alpha_to_number(alpha: str):
    result = 0
    for char in alpha:
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result


# ===== textLoader ===== #
def textLoader(fileName: str) -> list[list[str]]:
    """
    From file extension choose the loader.

    Args:
        - fileName (str): Name of the file.

    Returns:
        - list[list[str]], len = 2: The formatted text loaded from the file. (upper section & lower section)

    Raises:
        - ValueError: If the file extension is not .txt or .json.
    """
    extension = get_file_extension(fileName)
    if ".txt" == extension:
        return textfile_textLoader(fileName)
    if ".json" == extension:
        return json_textLoader(fileName)
    raise ValueError("File must have a .txt or .json extension")


def textfile_textLoader(fileName: str) -> list[list[str]]:
    """
    Loading file frome textfile (.txt) and formatting.

    Args:
        - fileName (str): Name of the file.

    Returns:
        - list[list[str]]: The formatted text loaded from the file. (upper section & lower section)
    """
    with open(fileName, "r", encoding="utf-8") as file:
        lines = [[], []]
        pointer = 0
        for line in file:
            line = line.replace("\t", "    ")

            if pointer < 1 and "" == line.strip():
                pointer += 1

            if line.strip() != "":
                lines[pointer].append(line)

        return lines

    print("Error: Fail to load from textfile.")


def json_textLoader(fileName: str):
    print("Error: Json will be supported soon.")  # TODO: .json
    pass

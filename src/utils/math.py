import math
from functools import reduce


def gcd_list(numbers: list[int]) -> int:
    """
    返回一个 List 的最大公约数。

    Args:
        - numbers (list[int])

    Returns:
        - int
    """
    if 0 == len(numbers):
        return 0
    return reduce(math.gcd, numbers)


def number_to_alpha(num: int, offset: int = 0) -> str:
    """
    数字转成字母（计算列号用）：`1 -> 'A'`

    Args:
        - num (int): 输入数字
        - offset (int): 偏移（方便计算）

    Returns:
        - str: (char)
    """
    number = num + offset
    alpha = ""
    while number > 0:
        number -= 1
        alpha = chr(number % 26 + ord("A")) + alpha
        number //= 26
    return alpha


def alpha_to_number(alpha: str) -> int:
    """
    字母转成数字：`A -> 1`

    Args:
        - alpha (str): 输入字符串

    Returns:
        - str: (char)
    """
    alpha = alpha.upper()
    result = 0
    for char in alpha:
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result

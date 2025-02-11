from pathlib import Path


def textLoader(file_name: str) -> list:
    """
    从文件加载文本，然后按照空行为界限分为上下两段（行标题和列标题）。

    Args:
        file_name (str): 要读取的文件路径。

    Returns:
        list: 包含两个列表的列表，分别表示上下段的内容。

    Raises:
        ValueError: 如果文件无法读取或格式不符合预期。
    """

    try:
        file_name = Path(file_name)
        with open(file_name, "r", encoding="utf-8") as file:
            sections = [[], []]  # 上下段
            current_section = 0

            for line in file:
                line = line.replace("\t", "    ")  # 部分地方导出的文件会有水平制表符

                # 切段
                if 0 == current_section and not line.strip():
                    current_section += 1
                    continue

                if line.strip():
                    sections[current_section].append(line)

            return sections

    except FileNotFoundError:
        raise ValueError(f"Error: File '{file_name}' not found.")
    except IOError:
        raise ValueError(f"Error: Unable to read file '{file_name}'.")
    except Exception as e:
        raise ValueError(f"Error: An unexpected error occurred while reading the file: {e}")

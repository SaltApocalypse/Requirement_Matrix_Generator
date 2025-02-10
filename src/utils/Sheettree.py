import re
import utils.math


class SheetTree:
    """
    树形结构
    需求矩阵的横纵各一棵
    """

    def __init__(self, file: str):
        """
        从文件创建指定树形结构

        Args:
            - fileName (str): 目前只支持 .txt 或 .json 文件
        """
        self.node_nums = 0  # 节点总数
        self.node_father = []  # 父节点
        self.node_level = []  # 节点层级，顶级为 0 级
        self.tree_depth = 0  # 树深度
        self.tree_data = []  # 当字典用，拿来记录对应的 "field name": {index : field name}

        self._branch = []  # 记录分支节点的栈

        self.__analyse_text(file)

    def __analyse_text(self, file: str) -> None:
        """
        建立并分析文本，形成指定树形结构

        Args:
            - fileName (str)
        """
        indent, prefix = self.__preprocess_text(file)  # 预处理

        # 对分好的每行：分出层级和内容，就可以加入树内了
        for line in file:
            level, data = self.__format_text(line, indent, prefix)
            self.__add_node(level, data)

    def __preprocess_text(self, file: list[str]) -> tuple[int, str]:
        """
        预处理，获得文本的缩进长度以及标记前缀

        Args:
            - file (list[str]): 预处理文本

        Returns:
            - (int) 缩进长度
            - (str) 标记前缀
        """
        sectionSpace = []
        for line in file:
            space = len(line) - len(line.lstrip())
            if space != 0:
                sectionSpace.append(space)

        sectionIndent = utils.math.gcd_list(sectionSpace)

        match = re.search(r"[^0-9a-zA-Z]", file[0])
        prefix = match.group() if match else ""

        return sectionIndent, prefix

    def __add_node(self, level: int, data: str) -> None:
        """
        往指定的树形结构上挂载分析好的节点

        Args:
            - level (int): 该单元格的缩进 The indentation level of this data, calculated by dividing the space length.
            - data (str): 该单元格的内容 The labels of the sheet.
        """
        # 处理父节点
        self.node_level.append(level)
        if level == 0:
            self.node_father.append(-1)  # root has no father
        else:
            self.node_father.append(self._branch[level - 1])

        # 处理分支
        while len(self._branch) > level:
            self._branch.pop()
        self._branch.append(self.node_nums)
        # tree & nodeNum++
        self.tree_data.append(data)
        self.tree_depth = max(self.tree_depth, level + 1)
        self.node_nums += 1

    def __format_text(self, text: str, space: int = 4, prefix: str = "") -> tuple[int, str]:
        """
        Remove leading indentations and prefix from the text (if any).

        Args:
            - text (str): Each line in file.
            - space (int): The length of indentation, default is 4.
            - prefix (str): The marker of text, "" if no prefix.

        Returns:
            - int: Level of indentation.
            - str: Adjusted formatted data.
        """
        data = text.strip()
        level = 0 if 0 == space else (len(text) - len(data)) // space

        # Remove prefix if it exists at the start of the data
        if data.startswith(prefix):
            data = data[len(prefix) :]
        data = data.lstrip()  # If there's any space after the prefix marker.

        return level, data

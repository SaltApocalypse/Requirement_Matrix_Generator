import re
import utils.math


class SheetTree:
    def __init__(self, section: str):
        """
        从文件创建指定树形结构。

        Args:
            section (str) : 分好的段落。
        """
        self.node_nums = 0  # 节点总数
        self.node_father = []  # 父节点
        self.node_level = []  # 节点层级，顶级为 0 级
        self.tree_depth = 0  # 树深度
        self.tree_data = []  # 当字典用，拿来记录对应的 "field name": {index : field name}
        self.branch = []  # 记录分支节点的栈

        self.__analyse_text(section)

    def __analyse_text(self, section: list) -> None:
        """
        建立并分析文本，形成指定树形结构。

        Args:
            - section (list[str]) : 分割好的段落。
        """
        indent, prefix = self.__preprocess_text(section)  # 预处理

        # 对分好的每行：分出层级和内容，就可以加入树内了
        for line in section:
            level, data = self.__format_text(line, indent, prefix)
            self.__add_node(level, data)

    def __preprocess_text(self, section: list[str]) -> tuple[int, str]:
        """
        预处理文本段落，获取缩进长度和标记前缀。

        Args:
            section (list[str]): 需要预处理的文本段落。

        Returns:
            tuple[int,str]: 返回一个元组，包含缩进长度和标记前缀。

        """
        sectionSpace = []
        for line in section:
            space = len(line) - len(line.lstrip())
            if space != 0:
                sectionSpace.append(space)

        sectionIndent = utils.math.gcd_list(sectionSpace)

        match = re.search(r"[^0-9a-zA-Z]", section[0])
        prefix = match.group() if match else ""

        return sectionIndent, prefix

    def __format_text(self, text: str, space: int = 4, prefix: str = "") -> tuple[int, str]:
        """
        调整格式（溢出开头缩进以及标记前缀符号）。

        Args:
            text (str): 段落中的每行内哦让那个。
            space (int): 缩进长度，默认为 4.
            prefix (str): 前缀，如果没有则为空。

        Returns:
            tuple[int,str]: 返回一个元组，包含缩进长度和标记前缀。
        """
        data = text.strip()
        level = 0 if 0 == space else (len(text) - len(data)) // space

        # 移除数据内容之前的前缀和缩进
        if data.startswith(prefix):
            data = data[len(prefix) :]
        data = data.lstrip()  # 移除前缀和数据内容之间的空格（如果有）

        return level, data

    def __add_node(self, level: int, data: str) -> None:
        """
        往指定的树形结构上挂载分析好的节点。

        Args:
            level (int): 该单元格的缩进。
            data (str): 该单元格的内容。
        """
        # 处理父节点
        self.node_level.append(level)
        self.node_father.append(-1 if level == 0 else self.branch[level - 1])  # 根节点没有父亲

        # 处理分支
        while len(self.branch) > level:
            self.branch.pop()
        self.branch.append(self.node_nums)
        # tree & nodeNum++
        self.tree_data.append(data)
        self.tree_depth = max(self.tree_depth, level + 1)
        self.node_nums += 1

import re

import utils


class SheetTree:
    def __init__(self, file: str):
        """
        Initialize the ExampleClass.

        Args:
            fileName (str): The name of the file to be processed. The file must have a .txt or .json extension.
        """
        self.node_nums = 0  # the total number of nodes
        self.node_father = []  # node's father
        self.node_level = []  # node's level
        self.tree_depth = 0  # tree's depth
        self.tree_data = []  # a dictionary to record "field name"s: {index : field name}

        self.__branch = []  # a stack for recording branch nodes

        self.__analyse_text(file)

    def __add_node(self, level: int, data: str) -> None:
        """
        Add analysed data as a node to the `SheetTree`.

        Args:
            - level (int): The indentation level of this data, calculated by dividing the space length.
            - data (str): The labels of the sheet.
        """
        # nodeFather
        self.node_level.append(level)
        if level == 0:
            self.node_father.append(-1)  # root has no father
        else:
            self.node_father.append(self.__branch[level - 1])

        # branch
        while len(self.__branch) > level:
            self.__branch.pop()
        self.__branch.append(self.node_nums)
        # tree & nodeNum++
        self.tree_data.append(data)
        self.tree_depth = max(self.tree_depth, level + 1)
        self.node_nums += 1

    def __preprocess_text(self, file: list[str]) -> tuple[int, str]:
        """
        Preprocess the file to determine the number of spaces for indentation and the prefix.

        Args:
            - file (list[str]): The file to be preprocessed.

        Returns:
            - (int) The number of spaces used for indentatio.
            - (str) The prefix at the beginning of each line in the file.
        """
        sectionSpace = []
        for line in file:
            space = len(line) - len(line.lstrip())
            if space != 0:
                sectionSpace.append(space)

        sectionIndent = utils.gcd_list(sectionSpace)

        match = re.search(r"[^0-9a-zA-Z]", file[0])
        prefix = match.group() if match else ""

        return sectionIndent, prefix

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

    def __analyse_text(self, file: str) -> None:
        """
        Analyse the text and create a "sheet tree".

        Args:
            - fileName (str): The name of the file containing raw text.
        """
        indent, prefix = self.__preprocess_text(file)
        for line in file:
            level, data = self.__format_text(line, indent, prefix)
            self.__add_node(level, data)

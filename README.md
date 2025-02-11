# Requirement Matrix Generator

需求矩阵生成器，通过一定格式的文本文件生成 `.xlsx` 的需求矩阵表格。

## 适用平台

Windows

## 使用方法

### 操作说明

- 下载项目并安装依赖库 `pip install openpyxl`
- 用终端打开项目文件夹，使用 `python src/main.py -i <inputFile>` 启动
- （可选，但是推荐）使用前运行下面的测试

### 测试

- 用终端打开项目文件夹，使用 `python src/main.py -i test.txt` 启动测试

### 文本文件格式

- **（建议：可参考测试文件）**
- 由两段文本组成，两段文本之间用空行隔开。（前一段为*行标题*，后一段为*列标题*）
- 上下级关系使用缩进表示。
- 缩进后添加一个半角符号和空格，然后是内容。

### 参数列表

#### 必填

- `--input_file, -i`: 输入文件路径

#### 可选
- `--output_path, -o`: `.xlsx`文件的输出目录。
- `--name -n`: 输出的`.xlsx`文件的名字。
- `--title -t`: 输出的需求矩阵的标题。

### Cheat Sheet

可以使用 <u>Markdown</u> 的无序列表来写文本，然后再在**源代码模式**下直接获取文本文件。

## 二次开发

### 开发

- 开发版本 python=3.11
- 第三方库 `pip install openpyxl`

# 感谢

- 使用了 Python 及其部分第三方库（见上）。

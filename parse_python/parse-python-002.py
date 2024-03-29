from tree_sitter import Language, Parser

# 如果需要遍历所有节点，可以使用递归函数
def traverse(node):
    print(node.type, node.start_byte, node.end_byte)
    for child in node.children:
        traverse(child)

# 加载构建的 Python 语言库
PYTHON_LANGUAGE = Language('../build/my-languages.so', 'python')

# 初始化解析器并设置语言
parser = Parser()
parser.set_language(PYTHON_LANGUAGE)

# code_file = "/home/richardliu/code/github.com/c4fun/zhipuai-playground/samples/gradio-glm4.py"
# code_file = "/home/richardliu/code/github.com/c4fun/llm-project-helper/llm_project_helper/repo_traverser.py"
code_file = "/home/richardliu/code/github.com/geekan/MetaGPT/tests/metagpt/tools/test_azure_tts.py"
# Python 代码片段，从文件中读取
with open(code_file, 'r') as file:
    python_code_snippet = file.read()

    # 解析代码
    tree = parser.parse(bytes(python_code_snippet, "utf8"))
    root_node = tree.root_node

    # 遍历语法树的直接子节点
    for child in root_node.named_children:
        print(child.type, child.start_byte, child.end_byte)

# 从根节点开始遍历
traverse(root_node)
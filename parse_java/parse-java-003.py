from tree_sitter import Language, Parser

# 如果需要遍历所有节点，可以使用递归函数
def traverse(node, identation_level):
    # write to 001-treesitter-parse-result.txt
    with open('003-loc-interface.txt', 'a') as f:
        for i in range(identation_level):
            f.write('  ')
        f.write(f'{node.type} {node.start_point} {node.end_point}\n')
    for child in node.children:
        traverse(child, identation_level+1)

# 加载构建的 Java 语言库
JAVA_LANGUAGE = Language('../build/my-languages.so', 'java')

# 初始化解析器并设置语言
parser = Parser()
parser.set_language(JAVA_LANGUAGE)

code_file = "/home/richardliu/code/github.com/rvesse/airline/airline-core/src/main/java/com/github/rvesse/airline/ChannelFactory.java"
# Java 代码片段，从文件中读取
with open(code_file, 'r') as file:
    java_code_snippet = file.read()

    # 解析代码
    tree = parser.parse(bytes(java_code_snippet, "utf8"))
    root_node = tree.root_node

    # 遍历语法树的直接子节点
    for child in root_node.named_children:
        print(child.type, child.start_byte, child.end_byte)

# 从根节点开始遍历
traverse(root_node, 0)

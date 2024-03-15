from tree_sitter import Language, Parser

# 注意C++对应cpp，C#对应c_sharp（！这里短横线变成了下划线）
# 看仓库名称
CPP_LANGUAGE = Language('build/my-languages.so', 'cpp')
CS_LANGUAGE = Language('build/my-languages.so', 'c_sharp')

# 举一个CPP例子
cpp_parser = Parser()
cpp_parser.set_language(CPP_LANGUAGE)

# 这是b站网友写的代码，解析看看
cpp_code_snippet = '''
int main{
  piantf("hell world");
  remake O;
}
'''

# 没报错就是成功
tree = cpp_parser.parse(bytes(cpp_code_snippet, "utf8"))
# 注意，root_node 才是可遍历的树节点
root_node = tree.root_node

# 孩子节点【节点数、节点列表】
root_node.child_count
root_node.children
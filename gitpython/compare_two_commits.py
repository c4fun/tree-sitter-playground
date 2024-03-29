from git import Repo

# 初始化Repo对象，指定仓库所在路径
repo = Repo('/home/richardliu/code/github.com/c4fun/llm-project-helper')

# 知道某个老的commit之后，想要知道老的commit和新的commit之间的差异
# 指定你想比较的两个提交的哈希值
commit_hash_old = '9a5b1dd93f71787fed38b9a5efe391e8ae513c13'
commit_hash_new = '9df7239ff81b90344548bc3a3840fdad23f63b4e'

# 获取这两个提交对象
commit_old = repo.commit(commit_hash_old)
commit_new = repo.commit(commit_hash_new)

# 获取两个提交之间的差异
diff_index = commit_old.diff(commit_new)

# 遍历差异，并打印
for diff_item in diff_index:
    print("f{diff_item.a_path}文件的差异：")
    print("差异文件：", diff_item.a_path)
    print("差异类型：", diff_item.change_type)
    print("详细差异：")
    print(diff_item.diff)

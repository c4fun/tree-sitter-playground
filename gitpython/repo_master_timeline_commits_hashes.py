from git import Repo

# 初始化Repo对象，指定仓库所在路径
repo = Repo('/home/richardliu/code/github.com/c4fun/llm-project-helper')

# 尝试获取master分支，如果失败则尝试获取main分支
try:
    branch = repo.branches['main']
except IndexError:
    branch = repo.branches['master']
    
# 获取分支的所有提交，由老到新
commits = list(reversed(list(branch.commit.iter_items(repo, branch.path))))

# 遍历提交
for commit in commits:
    print(commit.hexsha)
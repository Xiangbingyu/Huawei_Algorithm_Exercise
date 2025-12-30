n = int(input())
tree = {}
tree_v = {}
for i in range(n):
    a, b ,c  = map(int, input().split())
    if a not in tree:
        tree[a] = []
        tree_v[a] = []
    if b not in tree:
        tree[b] = []
        tree_v[b] = []
    tree[a].append(b)
    tree_v[a].append(c)

visited = {}
cycle = False

def has_cycle(node):
    global cycle
    if cycle:
        return
    if node in visited:
        if visited[node] == 1:
            cycle = True
        return
    visited[node] = 1
    if node in tree:
        for neighbor in tree[node]:
            has_cycle(neighbor)
    visited[node] = 2

for node in tree:
    if node not in visited:
        has_cycle(node)

if cycle:
    print('-1')
else:
    memo = {}
    memo_len = {}
    
    def dfs(node):
        if node in memo:
            return memo[node]
        if node not in tree or len(tree[node]) == 0:
            memo[node] = 0
            return 0
        max_sum = 0
        for i, neighbor in enumerate(tree[node]):
            max_sum = max(max_sum, tree_v[node][i] + dfs(neighbor))
        memo[node] = max_sum
        return max_sum
    
    def dfs_len(node):
        if node in memo_len:
            return memo_len[node]
        if node not in tree or len(tree[node]) == 0:
            memo_len[node] = 1
            return 1
        max_len = 1
        for neighbor in tree[node]:
            max_len = max(max_len, 1 + dfs_len(neighbor))
        memo_len[node] = max_len
        return max_len
    
    max_v = 0
    max_len = 0
    for node in tree:
        max_v = max(max_v, dfs(node))
        max_len = max(max_len, dfs_len(node))
    print(max_v, max_len)

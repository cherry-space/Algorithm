N, M = map(int, input().split())
list_num = []

def dfs(strt):
    if len(list_num) == M:
        print(' '.join(map(str, list_num)))
        return
    
    for i in range(strt, N+1):
        if i not in list_num:
            list_num.append(i)
            dfs(i+1)
            list_num.pop()
            

dfs(1)
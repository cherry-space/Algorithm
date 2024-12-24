import sys

dont_see = []
total = 0

N, M = map(int, input().split())

dont_listen = []
for _ in range(N):
    dont_listen.append(input().strip())

dont_see = []    
for _ in range(M):
    dont_see.append(input().strip())
    
result = sorted(set(dont_listen) & set(dont_see))

print(len(result))
for name in result:
    print(name)
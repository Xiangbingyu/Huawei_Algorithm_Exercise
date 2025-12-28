N = int(input())
X = list(map(int, input().split()))
M = int(input())
Y = list(map(int, input().split()))

new_list = X.copy()
manage_list = [1] * N

for j in range(M):
    k = Y[j]
    b = 1
    while(1):
        if k - b >= 0 and X[k] == X[k - b] and manage_list[k - b] != -1:
            new_list[k - b] = -1
            new_list[k] = X[k] + 1
            manage_list[k - b] = -1
            b += 1
        else:
            break

print(sum(1 for x in new_list if x != -1))

n = int(input())
v_list = list(map(int, input().split()))

cont = 0

for i in range(n):
    for j in range(i+1, n):
        if v_list[i] > v_list[j]*2:
            cont += 1
            break

print(cont)

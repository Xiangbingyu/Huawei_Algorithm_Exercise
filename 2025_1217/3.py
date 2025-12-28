n = int(input())
papers = list(map(int, input().split()))
left, right = map(int, input().split())

result = 0

for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += papers[j]
        if left <= current_sum <= right:
            result += 1

print(result)

# import bisect

# n = int(input())
# papers = list(map(int, input().split()))
# left, right = map(int, input().split())

# prefix = [0] * (n + 1)
# for i in range(n):
#     prefix[i + 1] = prefix[i] + papers[i]

# result = 0
# sorted_prefix = [0]

# for j in range(1, n + 1):
#     target_min = prefix[j] - right
#     target_max = prefix[j] - left
    
#     left_idx = bisect.bisect_left(sorted_prefix, target_min)
#     right_idx = bisect.bisect_right(sorted_prefix, target_max)
    
#     result += right_idx - left_idx
    
#     bisect.insort(sorted_prefix, prefix[j])

# print(result)
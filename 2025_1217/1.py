n, m = map(int, input().split())
a = list(map(int, input().split()))
x = [0] * m
y = [0] * m
for j in range(m):
    x[j], y[j] = map(int, input().split())

count_dict = {}
for num in a:
    count_dict[num] = count_dict.get(num, 0) + 1
max_a = max(a) if a else 0

for j in range(m):
    curr_x = x[j]
    curr_y = y[j]
    valid_nums = set()
    
    if curr_x == 0:
        target = 0 + curr_y
        if target in count_dict:
            valid_nums.add(target)
    elif curr_x == 1:
        target = 1 + curr_y
        if target in count_dict:
            valid_nums.add(target)
    else:
        k = 1
        while True:
            power = pow(curr_x, k)
            target = power + curr_y
            if target > max_a:
                break
            if target in count_dict:
                valid_nums.add(target)

            k += 1
    
    if not valid_nums:
        vis = 0
        max_peak = 0
    else:
        vis = sum(count_dict[num] for num in valid_nums)
        max_peak = max(count_dict[num] for num in valid_nums)
    
    print(vis, max_peak)

        
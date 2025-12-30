sample = list(map(list, input().split()))

result_dict = {}
for i in range(1, len(sample)):
    result = []
    match = 0
    for j in range(min(len(sample[i]), len(sample[0]))):
        if sample[i][j] == sample[0][j]:
            result.append(sample[i][j])
            match += 1
        if sample[i][j] != sample[0][j]:
            match = 0
            break
    if match != 0:
        result_str = ''.join(result)
        if result_str in result_dict:
            result_dict[result_str] += 1
        else:
            result_dict[result_str] = 1

if result_dict:
    for key in sorted(result_dict.keys(), key=len, reverse=True):
        print(key, result_dict[key])    
else:
    print('null')
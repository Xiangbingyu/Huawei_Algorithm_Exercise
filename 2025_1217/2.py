from functools import cmp_to_key

n = int(input())
v = []

for i in range(n):
    v.append(input())

def parse_string(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(('num', int(s[i:j])))
            i = j
        else:
            tokens.append(('char', s[i]))
            i += 1
    return tokens

def compare(a, b):
    tokens_a = parse_string(a)
    tokens_b = parse_string(b)
    
    i = 0
    while i < len(tokens_a) and i < len(tokens_b):
        type_a, val_a = tokens_a[i]
        type_b, val_b = tokens_b[i]
        
        if type_a == 'num' and type_b == 'num':
            if val_a < val_b:
                return -1
            elif val_a > val_b:
                return 1
        elif type_a == 'num' and type_b == 'char':
            return -1
        elif type_a == 'char' and type_b == 'num':
            return 1
        else:
            if val_a < val_b:
                return -1
            elif val_a > val_b:
                return 1
        i += 1
    
    if len(tokens_a) < len(tokens_b):
        return -1
    elif len(tokens_a) > len(tokens_b):
        return 1
    else:
        return 0

result = sorted(v, key=cmp_to_key(compare))

for item in result:
    print(item)

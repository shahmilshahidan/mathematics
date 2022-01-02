def permutations(string):
    #your code here
    result = []
    
    def permute(s, i, length):
        if i == length:
            result.append(''.join(s))
        else:
            for j in range(i, length):
                s[i], s[j] = s[j], s[i]
                permute(s, i+1, length)
                s[i], s[j] = s[j], s[i]
    
    permute(list(string), 0, len(string))
    result = eliminate_dups(result)
    return result

def eliminate_dups(res):
    clean_result = []
    res = sorted(res)
    for i in range(len(res)):
        if res[i] not in clean_result:
            clean_result.append(res[i])
        else:
            continue
    return clean_result

print(permutations('aabb'))
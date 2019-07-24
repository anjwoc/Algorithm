import operator
def solution(strings, n):
    answer = []
    dic = dict()
    
    for char in strings:
        dic[char] = char[n]
    print(dic.items())
    ret = sorted(dic.items(), key=operator.itemgetter(1,0))
    for val in ret:
        answer.append(val[0])
    return answer

strings = ["sun", "bed", "car"]	
n=1
strings2 = ["abce", "abcd", "cdx"]
n2=2
print(solution(strings, n))
print(solution(strings2, n2))

#다른 사람 풀이
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])


def strange_sort2(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings
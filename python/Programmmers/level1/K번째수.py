import itertools
def solution(array, commands):
    answer = []
    for val in range(len(commands)):
        i,j,k = commands[val]
        if(i==j):
            tmp = [array[i-1]]
        else:
            tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer

arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr, commands))
#return [5, 6, 3]

#다른 풀이법
def another_solution(array, commands):
    return list(map(lambda x:sorted(array[ x[0]-1 : x[1]] , commands)))

#좀더 보기 편하게 짜면
def another_solution2(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j])) [k-1])
    return answer

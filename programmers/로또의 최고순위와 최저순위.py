def mySolution(lottos, win_nums):
    answer = []

    level = {6:1, 5:2, 4:3, 3:4, 2:5, 0:6}
    
    zeros = lottos.count(0)
    same = len(set(lottos) & set(win_nums))
    
    def get_rank(key):
        if key in level:
            return level[key]
        else:
            return level[0]
    
    answer = [get_rank(zeros+same), get_rank(same)]
    return answer

def bestSolution(lottos, win_nums):
    answer = []

    zeros = lottos.count(0)
    same = len(set(lottos) & set(win_nums))
    
    answer = [7-max(zeros + same, 1), 7-max(same, 1)]
    return answer

def solution(begin, target, words):
    ans = [begin]
    if target not in words:
        return 0
    ans_cnt = 0
    while(len(words) != 0):
        for char in ans:
            tmp = []
            for word in words:
                cnt = 0
                for j in range(len(char)):
                    if char[j] != word[j]:
                        cnt += 1
                    if cnt == 2:
                        break
                if cnt == 1:
                    print(char, word)
                    tmp.append(word)
                    words.remove(word)
        ans_cnt += 1
        if target in tmp:
            print(target)
            return ans_cnt
        else:
            ans = tmp

    return 0


begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))

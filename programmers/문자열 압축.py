def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)+1):
        ans = ''
        cnt = 1
        prev = s[:i]
        print(prev)

        for j in range(i, len(s) + i, i):
            nxt = s[j:i+j]

            if prev == nxt:
                cnt += 1
            else:
                if cnt != 1:
                    ans += str(cnt) + prev
                else:
                    ans += prev

                prev = s[j:j+i]
                cnt = 1

        result.append(len(ans))

    return min(result)


print(solution("aabbaccc") == 7)

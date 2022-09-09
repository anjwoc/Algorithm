def solution_wrong(s):
    ans = -1
    i = 1

    while (len(s) > 0):
        if i == len(s):
            return 0

        prev = s[i-1]
        cur = s[i]

        if len(s) > 2 and prev == cur:
            s = s[:i-1] + s[i+1::]
            i = 1
            continue
        elif len(s) == 2:
            if prev == cur:
                return 1
            else:
                return 0

        i += 1

    return ans


def solution(s):
    ans = -1
    prev = None
    st = []

    for c in s:
        # print(c)
        if len(st) > 0 and c == st[-1]:
            st.pop()
            continue
        st.append(c)

    return 1 if len(st) == 0 else 0


print(solution('baabaa') == 1)
print(solution('cdcd') == 1)

def check(s):
    st = []

    for c in s:
        if len(st) == 0:
            st.append(c)
            continue
        else:
            if st[-1] == '[' and c == ']':
                st.pop()
                continue
            elif st[-1] == '{' and c == '}':
                st.pop()
                continue
            elif st[-1] == '(' and c == ')':
                st.pop()
                continue
            elif st[-1] == '[{' and c == '}]':
                st.pop()
                continue
            else:
                st.append(c)

    return 1 if len(st) == 0 else 0


def solution(s):
    ans = 0

    L = len(s)
    for i in range(len(s)):
        param = s[i:] + s[:i]
        val = check(param)
        ans += val

    return ans

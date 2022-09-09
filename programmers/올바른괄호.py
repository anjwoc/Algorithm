def solution(s):
    st = []

    for i in s:
        if i == '(':
            st.append(i)
            continue

        if len(st) == 0:
            return False
        else:
            st.pop()

    return len(st) == 0

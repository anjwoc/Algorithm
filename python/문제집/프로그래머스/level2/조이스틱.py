import string


alpha = dict([(char, idx) for idx, char in enumerate(string.ascii_uppercase)])
print(alpha)


def solution(name):
    ans = 0

    tmp = 0
    pos = []

    if 'A' in name:
        i = 0
        while i < len(name):
            if name[i] == 'A':
                for j in range(i, len(name)):
                    if name[j] != 'A':
                        break
                pos.append((i, j))

            i += 1
    a_len = 0
    if pos:
        if pos[-1][1] == len(name):
            a_len = len(pos[:-1]) + 1
        else:
            a_len = sum([i[1]-i[0] for i in pos])

    name = name.replace('A', '')
    for c in name:
        tmp = 0
        if c == 'A':
            continue
        if alpha[c] > 13:
            tmp = 26 - alpha[c]
        else:
            tmp = alpha[c]
        print(tmp)
        ans += tmp

    ans += (len(name)-1)
    # ans += a_len

    return ans


def solution2(name):
    answer = 0
    n = len(name)
    num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]

    for ch in name:
        answer += num_char[ord(ch) - ord('A')]

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer


def solution3(name):
    make_name = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    i, ans = 0, 0

    print(make_name)
    while True:
        ans += make_name[i]
        make_name[i] = 0

        if sum(make_name) == 0:
            break

        left, right = 1, 1
        while make_name[i - left] == 0:
            left += 1
        while make_name[i + right] == 0:
            right += 1

        ans += left if left < right else right
        i += (-left) if left < right else right
    return ans


# "JEROEN", "JAN",
names = ["JERAAAAOEAAN"]
# answers = [56, 23, ]

for idx, name in enumerate(names):
    print('-------------%d-------------' % (idx))
    print(solution3(name))
    print('-------------%d-------------' % (idx))

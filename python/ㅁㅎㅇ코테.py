def toCapCase(string):
    arr = string.split()
    ans = []
    for i in arr:
        ans.append(i[0].upper() + i[1:])

    return " ".join(ans)


def get_middle(str):
    return str[((len(str) - 1) // 2) : ((len(str)) // 2) + 1]


def solution(number):
    result = 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return result


def order_weight(string):
    res = []
    ret = []

    for i in string.split():
        weight = 0
        for j in i:
            weight += int(j)
        res.append((weight, i))

    for w, val in sorted(res):
        ret.append(val)
    return " ".join(ret)


def high_order_bitmask(word_size):
    mask_high = ""
    mask_low = ""
    for i in range(word_size // 2):
        mask_high += "1"
        mask_low += "0"
    return int(mask_high + mask_low, 2)


def validBraces(string):
    st = []
    for i in string:
        if i in ["(", "[", "{"]:
            st.append(i)
        else:
            if len(st) == 0:
                return False
            if st[-1] == "(" and i == ")":
                st.pop()
            elif st[-1] == "[" and i == "]":
                st.pop()
            elif st[-1] == "{" and i == "}":
                st.pop()
            else:
                return False
    if len(st) > 0:
        return False

    return True

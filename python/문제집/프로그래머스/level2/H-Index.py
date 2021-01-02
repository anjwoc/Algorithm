def solution(citations):
    idx = 0
    length = len(citations)

    citations.sort(reverse=True)

    while idx < length:
        if citations[idx] <= idx:
            break
        idx += 1

    return idx

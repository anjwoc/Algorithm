def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        start = mid + 1
    else:
        end = mid - 1

    return binary_search_recursion(target, start, end, data)


lst = [i**2 for i in range(11)]
target = 9
idx = binary_search_recursion(target, 0, len(lst) - 1, lst)
if idx:
    print(lst[idx])
else:
    print("None")

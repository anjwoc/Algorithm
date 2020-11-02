def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


lst = [i**2 for i in range(11)]
target = 9
idx = binary_search(target, lst)

if idx:
    print(lst[idx])
else:
    print("None")

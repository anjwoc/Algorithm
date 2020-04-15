"""
arr = list(input())
arr = list(map(int, arr))

for i in range(len(arr)):
    max_idx = i
    for j in range(i + 1, len(arr)):
        if arr[max_idx] < arr[j]:
            max_idx = j
    arr[max_idx], arr[i] = arr[i], arr[max_idx]

for i in arr:
    print(i, end="")


"""

arr = input()
for i in range(9, -1, 1):
    for j in arr:
        if int(j) == i:
            print(i, end="")

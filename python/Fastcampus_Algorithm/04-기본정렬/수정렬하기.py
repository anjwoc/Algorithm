n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    min_idx = i  # 가장 작은 원소 인덱스
    for j in range(i + 1, n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in arr:
    print(i)

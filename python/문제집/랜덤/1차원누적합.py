arr = [i for i in range(10)]
print(arr)

for i in range(1, 10):
    arr[i] = arr[i-1] + arr[i]

print(arr)

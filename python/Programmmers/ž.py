h = [6, 9, 5, 7, 4]

ans = [0] * len(h)
for i in range(len(h) - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        # print(i, j)
        print(h[i], h[j])
        if h[i] < h[j]:
            ans[i] = j + 1
            break
print(ans)

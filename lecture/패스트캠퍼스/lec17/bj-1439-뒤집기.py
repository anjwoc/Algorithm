data = input()

cnt1 = 0
cnt2 = 0

if data[0] == "1":
    cnt1 += 1
else:
    cnt2 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == "1":
            cnt1 += 1
        else:
            cnt2 += 1

print(min(cnt1, cnt2))
n = int(input())
char = ["1", "2", "4"]
ans = ""
while n > 0:
    n -= 1
    ans = char[n % 3] + ans
    n //= 3

print(ans)

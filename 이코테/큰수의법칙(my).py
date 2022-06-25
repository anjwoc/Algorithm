n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr, reverse=True)

div_num = m // k
add_cnt = m % k
ans = div_num * (sorted_arr[0] * k)
ans += sorted_arr[1] * add_cnt
  
print(ans)

#github - python/cpython의 직접 쓰여진 코드
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)

    while lo < hi:
        mid = (lo + hi)//2
        if a[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

mylist = [1,2,3,4,7,8,11,33]
print(bisect(mylist,3))
#이진 탐색은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘. 검색 속도가 아주 빠르다.
import bisect
print(bisect.bisect(mylist,7))

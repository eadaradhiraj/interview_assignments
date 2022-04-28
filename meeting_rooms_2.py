#Given an array of meeting time intervals
#consisting of start and end times[[s1,e1],[s2,e2],...](si< ei),
#find the minimum number of conference rooms required.

def sol(arr: list) -> int:
    arr.sort(key=lambda x: x[1])
    l, c, r = 0, 1, len(arr) - 1
    while l<=r:
        if arr[l][1] < arr[r][0]:
            l+=1
            r-=1
        elif arr[l][1] > arr[r][0]:
            r-=1
            c+=1
    return(c)

print(
  sol(arr=[[0, 30],[5, 10],[15, 20]])
)
print(
  sol(arr=[[7,10],[2,4]])
)

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
m = int(input())
x_t = list(map(int, input().split()))
x.sort()
for i in range(len(x_t)):
    start = 0
    end = len(x) - 1
    a = False
    while start <= end:
        mid = (start + end) //2
        
        if x[mid] > x_t[i]:
            end = mid - 1
        elif x[mid] < x_t[i]:
            start = mid + 1
        else:
            a = True
            break
    if a:
        print(1, end = " ")
    else:
        print(0, end = " ")

        
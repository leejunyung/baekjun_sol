import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
x = int(input())

s.sort()
count = 0
left = 0
right = n-1

while left < right:
    temp = s[left] + s[right]
    if temp == x:
        count += 1
        left += 1
    elif temp > x:
        right -= 1
    else: 
        left += 1
print(count)
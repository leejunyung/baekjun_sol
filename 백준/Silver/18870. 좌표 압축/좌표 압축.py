import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
arr = sorted(set(x))
dic = {}

for i in range(len(arr)):
    dic[arr[i]] = i
for i in x:
    print(dic[i], end= " ")
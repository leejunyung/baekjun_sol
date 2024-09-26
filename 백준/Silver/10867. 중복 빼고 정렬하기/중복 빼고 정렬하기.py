import sys
input = sys.stdin.readline

n = int(input())
number = list(set(map(int, input().split())))
number.sort()
print(*number)
import sys
input = sys.stdin.readline
li_len, li_sum = map(int,input().split())
len_list = list(map(int,input().split()))
sum_list = [0]
sum_temp = 0
for j in len_list:
    sum_temp += j
    sum_list.append(sum_temp)
for i in range(li_sum):
    a,b = map(int,input().split())
    print(sum_list[b]-sum_list[a-1])
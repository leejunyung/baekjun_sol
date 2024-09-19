import sys
input = sys.stdin.readline

n = int(input())
li = []
c_li = []
n_sum = 0
count = dict()
for i in range(n):
    num = int(input())
    li.append(num)
    n_sum += num
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1
a_mean = round(n_sum / n)
li.sort()
mid = int(n/2)
mid_num = li[mid]
print(a_mean)
print(mid_num)
max_fre = max(count.values())
count_fre = []
for j, l in count.items():
    if l == max_fre:
        count_fre.append(j)
if len(count_fre) == 1:
    print(count_fre[0])
else:
    print(sorted(count_fre)[1])
num_range = li[n-1] - li[0]
print(num_range)
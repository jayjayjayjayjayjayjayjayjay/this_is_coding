import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum=0
a=0
for j in range(n):
    if j+m < n:
        for i in range(m):
            sum+=arr[j+i]
    if a<sum:
        a=sum
    sum =0

print(a)



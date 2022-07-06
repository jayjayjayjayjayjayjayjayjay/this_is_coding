n,m = map(int,input().split())

for i in range(n):
    data = list(map(int, input().split()))
    if i==0:
        result = data[0]
    min_value = min(data)
    result = min(result,min_value)

print(result)

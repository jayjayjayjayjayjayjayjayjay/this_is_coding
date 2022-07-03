n, m, k = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()
first_num = nums[n-1]
second_num = nums[n-2]

result =0

while 1:
    for i in range(k):
        result += first_num
        m -=1
    result += second_num
    m-=1
    if m ==0:
        break
print(result)




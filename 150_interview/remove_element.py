nums = list(map(int , input().split()))
val = int(input())
while val in nums:
    nums.remove(val)
    nums.append("_")
print(*nums)
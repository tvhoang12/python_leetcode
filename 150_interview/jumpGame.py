nums = [2,3,1,1,4]
dp = [0 for _ in range(len(nums))]
dp[0] = 1
ok = False
for i in range(len(nums)):
    if dp[i] > 0:
        # print("here")
        print(*dp)
        for j in range(nums[i] + 1):
            dp[i + j] += 1
            if i + j == len(nums) - 1:
                ok = True
                break
print("yes" if ok else print("no"))
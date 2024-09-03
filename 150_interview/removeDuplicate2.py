class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[dup]:
                if nums[dup - 1] != nums[dup]:
                    nums[dup + 1] = nums[i]
                    dup += 1
            else:
                nums[dup + 1] = nums[i]
                dup += 1
        return dup + 1
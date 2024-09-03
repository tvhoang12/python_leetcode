class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  

        seen = {}

        for index, item in enumerate(nums):
            seen[item] = index

        for index, item in enumerate(nums):
            n = target - item
            if n in seen and seen[n] != index:
                return [index, seen[n]]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if num in h:
                return [nums.index(diff), idx]
            else:
                h[diff] = 1
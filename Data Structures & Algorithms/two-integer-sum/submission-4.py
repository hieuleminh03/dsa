class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in h:
                return [h[diff], idx]
            h[num] = idx
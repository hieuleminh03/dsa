class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for num in nums:
            if num not in val:
                val[num] = 0
            val[num] += 1
        ans = sorted(val.items(), key = lambda item: item[1], reverse=True)
        return [item[0] for item in ans[:k]]


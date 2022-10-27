class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occur = set()
        for i in nums:
            if i in occur: occur.remove(i)
            else: occur.add(i)
        return list(occur)[0]
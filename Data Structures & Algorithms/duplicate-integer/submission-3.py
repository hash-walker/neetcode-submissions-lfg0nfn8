class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in range(0,len(nums)):
            freq[nums[i]] = 1
        return len(freq) != len(nums)
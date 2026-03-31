class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        for num in nums:
            length = 0
            if (num - 1) in set_nums:
                continue
            i=0
            while num + i in set_nums:
                length+=1
                if length> max_length:
                    max_length = length
                i+=1
        return max_length

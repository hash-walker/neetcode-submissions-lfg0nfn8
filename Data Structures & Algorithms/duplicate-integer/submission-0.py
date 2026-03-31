class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicate = {num for num in nums}

        if len(nums) > len(no_duplicate):
            return True
        
        return False
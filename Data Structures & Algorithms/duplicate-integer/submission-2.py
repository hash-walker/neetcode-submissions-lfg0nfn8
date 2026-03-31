class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # no_duplicate = {num for num in nums}

        # if len(nums) > len(no_duplicate):
        #     return True
        
        # return False


        for i, num in enumerate(nums):
            for j in range(1, len(nums)):
                if i != j and num == nums[j]:
                    return True

        return False
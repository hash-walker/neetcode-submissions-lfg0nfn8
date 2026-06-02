class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        duplicate = defaultdict(int)

        for num in nums:
            duplicate[num] += 1

            if duplicate[num] >= 2:
                return True
            
        return False
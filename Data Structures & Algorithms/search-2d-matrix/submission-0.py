class Solution:

    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1

        

        while s <= e:
            m = s + (e-s) // 2

            if nums[m] > target:
                e = m - 1
            elif nums[m] < target:
                s = m + 1
            else:
                return m
        
        return -1
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i, a_list in enumerate(matrix):
            search = self.search(a_list, target)

            if search == -1:
                continue
            
            return True
        
        return False
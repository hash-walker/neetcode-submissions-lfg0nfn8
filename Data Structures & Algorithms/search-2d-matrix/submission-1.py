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
                return nums[m]
        
        return nums[e]

    
    
    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        s = 0
        e = len(matrix) -1


        
        while s <= e:

            m = s + (e-s) // 2

            res = self.search(matrix[m], target)

            if res > target:
                e = m - 1
            elif res < target:
                s = m + 1
            else:
                return True        
        
        return False
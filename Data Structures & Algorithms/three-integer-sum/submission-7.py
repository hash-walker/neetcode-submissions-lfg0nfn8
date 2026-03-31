class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        for i in range(0,len(nums)):

            num = nums[i]
            if i>0:
                print("Here num[i]:" ,nums[i]," and nums[i-1]",nums[i-1],"and ",nums[i] == nums[i-1])
            if i >0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                partial_sum = nums[left]+nums[right]
                if partial_sum+num < 0:
                    left = left+1
                elif partial_sum+num > 0:
                    right = right - 1
                elif partial_sum+num == 0:
                    res.append([num,nums[left],nums[right]])
                    left = left+1
                    right = right -1
                    while left<len(nums) and nums[left] == nums[left-1]:
                        left = left+1
                

            
            
        return res


                

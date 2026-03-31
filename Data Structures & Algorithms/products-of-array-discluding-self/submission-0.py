class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zeros = 0
        for num in nums:
            if num:
                total_prod *= num
            else:
                zeros += 1
        if zeros>1: return [0]*len(nums)

        res = []
        for num in nums:
            if zeros and num: res.append(0)
            elif zeros:
                res.append(total_prod)
            else:
                res.append(total_prod//num)
        return res
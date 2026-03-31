class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) -1
        while l < r:
            mid = (l+r) //2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        pivot = l

        def binarysearch(l,r,target):
            while l<=r:
                mid = (l+r) //2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return -1
        
        res = binarysearch(0,pivot-1,target)
        if res == -1:
            res = binarysearch(pivot,len(nums)-1,target)
        return res

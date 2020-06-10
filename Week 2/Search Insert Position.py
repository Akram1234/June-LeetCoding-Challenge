from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return l




arr= [1,3,5,6]
target = 0
ans = Solution().searchInsert(arr, target)
print(ans)
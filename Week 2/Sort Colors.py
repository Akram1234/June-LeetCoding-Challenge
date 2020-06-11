from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def swap(a,b):
        #     nums[a], nums[b] = nums[b],nums[a]
        p0, p1, p2 = 0, 0, len(nums)
        while p1 < p2:
            if nums[p1] == 0:
                nums[p1], nums[p0] = nums[p0], nums[p1]
                p0, p1 = p0 + 1, p1 + 1
            elif nums[p1] == 1:
                p1 += 1
            else:
                p2 -= 1
                nums[p1], nums[p2] = nums[p2], nums[p1]



inp_arr = [2,0,2,1,1,0]
Solution().sortColors(inp_arr)
print(inp_arr)
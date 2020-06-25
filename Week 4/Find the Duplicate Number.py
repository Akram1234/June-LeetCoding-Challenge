class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # a=list(set(nums))

        hare = nums[0]
        tortoise = nums[0]
        while True:
            
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break
        ptr = nums[0]
        while ptr!=tortoise:
            ptr = nums[ptr]
            tortoise = nums[tortoise]
        return ptr

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for i in nums:
            twos = twos | (i&ones)
            ones = ones ^ i
            threes = ones&twos
            ones = ones & ~threes
            twos = twos & ~threes
        return ones
        

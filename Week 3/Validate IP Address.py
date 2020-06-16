class Solution(object):
    def validIPAddress(self, IP):
        nums = IP.split('.')
        if len(nums) == 4:
            for i in range(len(nums)):
                not_digit = not nums[i].isdigit()
                if not_digit or (nums[i][0] == '0' and len(nums[i]) > 1) or not 0 <= int(nums[i]) < 256:
                    return "Neither"
            return "IPv4"

        nums = IP.split(':')
        if len(nums) == 8:
            for i in range(len(nums)):
                any_non_hexdigits = not all(c in string.hexdigits for c in nums[i])
                if not (1 <= len(nums[i]) <= 4) or any_non_hexdigits:
                    return "Neither"
            return "IPv6"
        return "Neither"

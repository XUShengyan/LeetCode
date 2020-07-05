# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3: 
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
###################################

class Solution:
    def reverse(self, x: int) -> int:
        if x >0:
            floorDivision = x
            negativFlag =0
        else:
            floorDivision = -x
            negativFlag = 1
        number = list()
        i =0

        while(floorDivision):
            remainder = floorDivision%10
            number.append(remainder)
            i = i +1
            floorDivision = floorDivision // 10

        result =0
        for i in range(i):
            result = number.pop() * 10**i + result
        if (2 ** -31 < result < 2 ** 31):
            if negativFlag:
                return -result
            else:
                return result
        else:
            return 0


test = Solution()
temp =test.reverse(-123)
print(temp)
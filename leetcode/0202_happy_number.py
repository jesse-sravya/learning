from helpers.test_helper import TestHelper
# sq_cache = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}

class Solution:
    def isHappy(self, n: int) -> bool:
        covered_nums = {}
    
        def isHappyRecursive(n: int) -> bool:
            if n in covered_nums:
                return False
            else:
                covered_nums[n] = None
    
            digits = [int(x)*int(x) for x in [int(x) for x in str(n)]]
            if len(digits) == 1 and digits[0] == 1:
                return True
            else:
                return isHappyRecursive(sum(digits))
        return isHappyRecursive(n)


TestHelper.test(Solution().isHappy(7), True)
TestHelper.test(Solution().isHappy(2), False)
TestHelper.test(Solution().isHappy(19), True)
TestHelper.test(Solution().isHappy(1111111), True)

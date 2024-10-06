from typing import List
from helpers.test_helper import TestHelper
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while index >= 0 and carry:
            digits[index] = digits[index] + carry
            carry = digits[index] // 10
            digits[index] = digits[index] % 10
            index -= 1

        return digits if not carry else [carry] + digits


TestHelper.test(Solution().plusOne([8, 9, 9]), [9, 0, 0])
TestHelper.test(Solution().plusOne([1, 2, 3]), [1, 2, 4])
TestHelper.test(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
TestHelper.test(Solution().plusOne([9]), [1, 0])
TestHelper.test(Solution().plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [
                9, 8, 7, 6, 5, 4, 3, 2, 1, 1])

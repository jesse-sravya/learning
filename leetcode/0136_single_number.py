from typing import List
from helpers.test_helper import TestHelper


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 1
        while index < len(nums):
            val = nums[index]
            if nums[index] in nums[0:index]:
                nums.remove(nums[index])
                nums.pop(index-1)
                index -= 1
            else:
                index += 1
        return nums[0]


class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        result = 0
        for item in nums:
            result ^= item
        return result


TestHelper.test(Solution().singleNumber2([2, 2, 1]), 1)
TestHelper.test(Solution().singleNumber2([4, 1, 2, 1, 2]), 4)
TestHelper.test(Solution().singleNumber2([1]), 1)
TestHelper.test(Solution().singleNumber2([1, 3, 1, -1, 3]), -1)
TestHelper.test(Solution().singleNumber2(
    [1, 1, 2, 3, 4, 5, 4, 5, 3, -1, 2]), -1)

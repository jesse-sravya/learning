from typing import List
from helpers.test_helper import TestHelper


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        gain = [0] + gain
        print(gain)
        for index in range(len(gain) - 1):
            gain[index + 1] = gain[index + 1] + gain[index]
            if gain[index + 1] > highest:
                highest = gain[index + 1]
        return highest


TestHelper.test(Solution().largestAltitude([-5, 1, 5, 0, -7]), 1)
TestHelper.test(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]), 0)

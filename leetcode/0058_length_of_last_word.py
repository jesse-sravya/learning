from helpers.test_helper import TestHelper


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


TestHelper.test(Solution().lengthOfLastWord("   fly me   to   the moon  "), 4)
TestHelper.test(Solution().lengthOfLastWord("   fly me   to   the moo"), 3)
TestHelper.test(Solution().lengthOfLastWord("m"), 1)
TestHelper.test(Solution().lengthOfLastWord("mmm mmm"), 3)

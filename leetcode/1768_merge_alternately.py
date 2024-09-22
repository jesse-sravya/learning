from test_helper import TestHelper


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        output = ""
        while (i < len(word1) and i < len(word2)):
            output += word1[i] + word2[i]
            i += 1

        output += word1[i:]
        output += word2[i:]
        return output


TestHelper.test(Solution().mergeAlternately("abc", "pqr"), "apbqcr")
TestHelper.test(Solution().mergeAlternately("ab", "pqrs"), "apbqrs")
TestHelper.test(Solution().mergeAlternately("abcd", "pq"), "apbqcd")

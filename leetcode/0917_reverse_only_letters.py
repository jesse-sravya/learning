from helpers.test_helper import TestHelper


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


TestHelper.test(Solution().reverseOnlyLetters("ab-cd"), "dc-ba")
TestHelper.test(Solution().reverseOnlyLetters(
    "a-bC-dEf-ghIj"), "j-Ih-gfE-dCba")

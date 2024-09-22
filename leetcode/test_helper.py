
class TestHelper:
    @staticmethod
    def test(actual, expected):
        print("returned:", actual)
        print("status:", actual == expected)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        result = 1
        for i in range(1, n+1):
            result *= i
        for i in str(result)[::-1]:
            if i == "0":
                c += 1
            else:
                break
        return c


class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution.trailingZeroes(5))

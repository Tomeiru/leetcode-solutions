# Time: O(N)
# Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        while begin < end:
            while begin < end and not s[begin].isalnum():
                begin += 1
            while end > begin and not s[end].isalnum():
                end -= 1
            if begin > end:
                break
            if s[begin].lower() != s[end].lower():
                return False
            begin += 1
            end -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isPalindrome("A man, a plan, a canal: Panama")}")
    print(f"Example 2: {solution.isPalindrome("race a car")}")
    print(f"Example 3: {solution.isPalindrome(" ")}")

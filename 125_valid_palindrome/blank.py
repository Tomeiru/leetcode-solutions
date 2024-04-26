# Time: O()
# Space: O()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return False

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isPalindrome("A man, a plan, a canal: Panama")}")
    print(f"Example 2: {solution.isPalindrome("race a car")}")
    print(f"Example 3: {solution.isPalindrome(" ")}")

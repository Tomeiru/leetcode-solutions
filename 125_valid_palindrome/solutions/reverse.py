# Time: O(N)
# Space: O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()
        return clean == clean[::-1]

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isPalindrome("A man, a plan, a canal: Panama")}")
    print(f"Example 2: {solution.isPalindrome("race a car")}")
    print(f"Example 3: {solution.isPalindrome(" ")}")

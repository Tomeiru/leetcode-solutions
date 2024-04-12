# Time: O(1) for early return otherwise O(nlogn)
# Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isAnagram("anagram", "nagaram")}")
    print(f"Example 2: {solution.isAnagram("rat", "car")}")

# Time: O(nlogn)
# Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isAnagram("anagram", "nagaram")}")
    print(f"Example 2: {solution.isAnagram("rat", "car")}")

from typing import Dict

# Time: O(1) for early return otherwise O(n)
# Space: O(1) for early return otherwise O(n)
class Solution:
    def generateDict(self, s: str) -> Dict[str, int]:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.generateDict(s) == self.generateDict(t)

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.isAnagram("anagram", "nagaram")}")
    print(f"Example 2: {solution.isAnagram("rat", "car")}")

from typing import List

# Time: O()
# Space: O()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [[]]


if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])}")
    print(f"Example 2: {solution.groupAnagrams([""])}")
    print(f"Example 3: {solution.groupAnagrams(["a"])}")

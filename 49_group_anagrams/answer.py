from typing import List, Dict

# Time: O(M * NlogN) where M is the number of string and N the average length of a string
# Space: O(N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[str,List[str]] = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in groups:
                groups[ss] = []
            groups[ss].append(s)
        return list(groups.values())

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])}")
    print(f"Example 2: {solution.groupAnagrams([""])}")
    print(f"Example 3: {solution.groupAnagrams(["a"])}")

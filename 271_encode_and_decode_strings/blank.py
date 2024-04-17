from typing import List

# Time: O()
# Space: O()
class Solution:
    def encode(self, strs: List[str]) -> str:
        return ""

    def decode(self, s: str) -> List[str]:
        return []

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.decode(solution.encode(["neet","code","love","you"]))}")
    print(f"Example 2: {solution.decode(solution.encode(["we","say",":","yes"]))}")

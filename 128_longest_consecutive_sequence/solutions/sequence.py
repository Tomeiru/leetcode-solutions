from typing import List

# Time: O(N)
# Space: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0
        for num in s:
            if num - 1 in s:
                continue
            consecutive = 1
            while num + consecutive in s:
                consecutive += 1
            result = max(consecutive, result)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.longestConsecutive([100,4,200,1,3,2])}")
    print(f"Example 1: {solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])}")


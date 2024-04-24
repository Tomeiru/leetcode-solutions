from typing import List

# Time: O(NlogN)
# Space: O(1) if sorted in place, here O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(set(nums))
        result = 1
        current = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                current += 1
            else:
                result = max(current, result)
                current = 1
        result = max(current, result)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.longestConsecutive([100,4,200,1,3,2])}")
    print(f"Example 2: {solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])}")


from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matchs = {}
        for index, num in enumerate(nums):
            matchs[target - num] = index
        for index, num in enumerate(nums):
            significant_other = matchs.get(num)
            if significant_other and index != significant_other:
                return [index, significant_other]
        return []

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.twoSum([2,7,11,15], 9)}")
    print(f"Example 2: {solution.twoSum([3,2,4], 6)}")
    print(f"Example 3: {solution.twoSum([3,3], 6)}")

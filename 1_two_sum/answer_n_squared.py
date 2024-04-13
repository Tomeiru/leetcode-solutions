from typing import List

# Time: O(n^2)
# Space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for ii in range(i + 1, len(nums)):
                print(nums[i] + nums[ii], i, ii)
                if nums[i] + nums[ii] == target:
                    return [i, ii]
        return []

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.twoSum([2,7,11,15], 9)}")
    print(f"Example 2: {solution.twoSum([3,2,4], 6)}")
    print(f"Example 3: {solution.twoSum([3,3], 6)}")
 

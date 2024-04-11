from typing import List

# Time: O(nlogn)
# Space: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.containsDuplicate([1,2,3,1])}")
    print(f"Example 2: {solution.containsDuplicate([1,2,3,4])}")
    print(f"Example 3: {solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")


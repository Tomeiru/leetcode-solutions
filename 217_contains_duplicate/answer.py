from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.containsDuplicate([1,2,3,1])}")
    print(f"Example 2: {solution.containsDuplicate([1,2,3,4])}")
    print(f"Example 3: {solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")


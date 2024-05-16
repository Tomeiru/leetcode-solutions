from typing import List

# Time: O(N^2)
# Space: O(N) but could be O(1) if I sorted in place
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    answers.append([sorted_nums[left], sorted_nums[right], sorted_nums[i]])
                    left += 1
                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
                        continue
        return answers

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.threeSum([-1,0,1,2,-1,-4])}")
    print(f"Example 2: {solution.threeSum([0,1,1])}")
    print(f"Example 3: {solution.threeSum([0,0,0])}")


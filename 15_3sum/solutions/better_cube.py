from typing import List

# Time: O(N^3)
# Space: O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for ii in range(i + 1, len(nums)):
                if ii > i + 1 and nums[ii] == nums[ii - 1]:
                    continue
                for iii in range(ii + 1, len(nums)):
                    if iii > ii + 1 and nums[iii] == nums[iii - 1]:
                        continue
                    if nums[i] + nums[ii] + nums[iii] == 0:
                        answers.append([nums[i], nums[ii], nums[iii]])
        return answers

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.threeSum([-1,0,1,2,-1,-4])}")
    print(f"Example 2: {solution.threeSum([0,1,1])}")
    print(f"Example 3: {solution.threeSum([0,0,0])}")


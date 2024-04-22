from typing import List

# Time: O(N)
# Space: O(1) if the output array doesn't count as extra space for analysis
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.productExceptSelf([1,2,3,4])}")
    print(f"Example 1: {solution.productExceptSelf([-1,1,0,-3,3])}")

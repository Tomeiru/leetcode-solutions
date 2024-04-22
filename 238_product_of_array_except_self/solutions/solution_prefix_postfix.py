from typing import List

# Time: O(N)
# Space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        answer = [0] * len(nums)
        x = 1
        y = 1
        for i in range(0, len(nums)):
            x *= nums[i]
            y *= nums[len(nums) - 1 - i]
            prefix[i] = x
            postfix[len(nums) - 1 - i] = y
        for i in range(0, len(nums)):
            pre = 1 if i == 0 else prefix[i - 1]
            post = 1 if i == len(nums) - 1 else postfix[i + 1]
            answer[i] = pre * post
        return answer

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.productExceptSelf([1,2,3,4])}")
    print(f"Example 1: {solution.productExceptSelf([-1,1,0,-3,3])}")

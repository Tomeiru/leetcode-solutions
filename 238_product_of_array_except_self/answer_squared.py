from typing import List

# Time: O(N^2)
# Space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(0, len(nums)):
            current = 1
            for ii in range(0, len(nums)):
                if i == ii:
                    continue
                current *= nums[ii]
            answer.append(current)
        return answer


if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.productExceptSelf([1,2,3,4])}")
    print(f"Example 1: {solution.productExceptSelf([-1,1,0,-3,3])}")

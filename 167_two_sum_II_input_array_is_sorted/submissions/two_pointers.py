from typing import List

# Time: O()
# Space: O()
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin = 0
        end = len(numbers) - 1
        while begin < end:
            result = numbers[begin] + numbers[end]
            if result == target:
                return [begin + 1, end + 1]
            if result > target:
                end -= 1
            else:
                begin += 1
        return []

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.twoSum([2,7,11,15], 9)}")
    print(f"Example 2: {solution.twoSum([2,3,4], 6)}")
    print(f"Example 3: {solution.twoSum([-1,0], 0)}")


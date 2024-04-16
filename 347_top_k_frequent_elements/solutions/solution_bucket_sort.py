from typing import List, Dict

# Time: O(N)
# Space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d: Dict[int, int] = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        bucket = [[] for _ in range(0, len(nums))]
        for num, occurence in d.items():
            bucket[occurence - 1].append(num)
        solutions = []
        for mostFrequentNums in reversed(bucket):
            if len(solutions) == k:
                break
            for mostFrequentNum in mostFrequentNums:
                solutions.append(mostFrequentNum)
        return solutions

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.topKFrequent([1,1,1,2,2,3], 2)}")
    print(f"Example 2: {solution.topKFrequent([1], 1)}")

from typing import List

# Time: O(NlogN)
# Space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        sd = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return list(sd.keys())[0:k]


if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.topKFrequent([1,1,1,2,2,3], 2)}")
    print(f"Example 2: {solution.topKFrequent([1], 1)}")

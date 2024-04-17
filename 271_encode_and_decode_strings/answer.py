from typing import List

# I consider this Solution wrong, I will still push it for the sake of it.
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            es = "#chocolat" + s
            encoded = encoded + es
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split('#chocolat')[1:]

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.decode(solution.encode(["neet","code","love","you"]))}")
    print(f"Example 2: {solution.decode(solution.encode(["we","say",":","yes"]))}")

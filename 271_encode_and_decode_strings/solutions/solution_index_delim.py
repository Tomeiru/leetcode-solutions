from typing import List

# Time: O(N)
# Space: O(N)
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            num_len = 0
            while s[i + num_len].isdigit():
                num_len += 1
            word_len = int(s[i:i + num_len])
            word_start = i + num_len + 1
            decoded.append(s[word_start:word_start + word_len])
            i += num_len + 1 + word_len
        return decoded

if __name__ == '__main__':
    solution = Solution()
    print(f"Example 1: {solution.decode(solution.encode(["neet","code","love","you"]))}")
    print(f"Example 2: {solution.decode(solution.encode(["we","say",":","yes"]))}")

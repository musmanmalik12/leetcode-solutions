# Problem: Longest Common Prefix (LeetCode)
# Approach: Start with first string as prefix and shrink until it matches all strings
# Time Complexity: O(n * m)
# Space Complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
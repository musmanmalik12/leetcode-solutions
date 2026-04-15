# Problem: Roman to Integer (LeetCode)
# Approach: Use hashmap + check next character for subtraction rule
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:

        rom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and rom[s[i]] < rom[s[i + 1]]:
                total -= rom[s[i]]
            else:
                total += rom[s[i]]

        return total
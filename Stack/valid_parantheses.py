# Problem: Valid Parentheses (LeetCode)
# Approach: Stack to match opening and closing brackets
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        sett = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stk = []
        for ch in s:

            # Case opening bracket : push to stack
            if ch in sett:
                stk.append(ch)

            # Otherwise, it must be a closing bracket
            else:
                if not stk:
                    return False
                top = stk.pop()
                # Check if it matches current closing bracket
                if sett[top] != ch:
                    return False

        # Empty stack means all brackets matched correctl; will return True, otherwise False
        return len(stk) == 0
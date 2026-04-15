# Problem: Palindrome Number (LeetCode)
# Approach: Use two pointers from both ends of the string representation
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_to_string = str(x)
        a = 0
        b = len(number_to_string) - 1

        for i in range(len(number_to_string)):
            if number_to_string[a] == number_to_string[b]:
                a += 1
                b -= 1
            else:
                return False

        return True
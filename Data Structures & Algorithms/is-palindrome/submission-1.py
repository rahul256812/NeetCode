class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 1. Clean the string using a standard loop
        clean_s = []
        for char in s:
            if char.isalnum():
                clean_s.append(char.lower())
                
        # 2. Run your Two-Pointer logic
        left = 0
        right = len(clean_s) - 1
        
        while right > left:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
            
        return True
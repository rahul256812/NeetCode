class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) == len(t):
            for i in range(len(s)):
                # For string s
                if s[i] in dict1:
                    dict1[s[i]] += 1  # Increment if already seen
                else:
                    dict1[s[i]] = 1   # Initialize to 1 if first time
                
                # For string t (check in dict2, not dict1!)
                if t[i] in dict2:
                    dict2[t[i]] += 1  # Increment if already seen
                else:
                    dict2[t[i]] = 1   # Initialize to 1 if first time
        else:
            return False

        return dict1 == dict2
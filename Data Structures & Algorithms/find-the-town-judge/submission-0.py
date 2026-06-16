class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Array to store the net trust score for each person
        # Index 0 is ignored since people are labeled 1 to n
        trust_scores = [0] * (n + 1)
        
        for a, b in trust:
            # Person 'a' loses a point because they trust someone
            trust_scores[a] -= 1
            # Person 'b' gains a point because they are trusted
            trust_scores[b] += 1
            
        # Look for the person who has a net trust score of exactly n - 1
        for person in range(1, n + 1):
            if trust_scores[person] == n - 1:
                return person
                
        return -1

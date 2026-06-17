class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        count=Counter(s)
        for i in t:
            count[i]-=1
            if count[i]<0:
                return i
        

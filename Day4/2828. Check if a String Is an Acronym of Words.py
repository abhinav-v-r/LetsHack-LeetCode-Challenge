class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acro=""
        for i in words:
            acro+=i[0]
        return acro==s
            

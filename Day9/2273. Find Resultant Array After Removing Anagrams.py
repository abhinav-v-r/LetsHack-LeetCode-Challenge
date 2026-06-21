class Solution:
    def checkAnagram(self,a,b):
        return sorted(a)==sorted(b)
        
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        for i in range(1,len(words)):
            if not self.checkAnagram(words[i],res[-1]):
               res.append(words[i])
        return res

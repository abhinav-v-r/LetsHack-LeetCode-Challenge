class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0, 0]
        arr = []
        
        for i in grid:
            for j in i:
                arr.append(j)
        count = len(arr)
        for i in range(1, count + 1):
            if arr.count(i)==2:
                ans[0] = i
            elif arr.count(i)==0:
                ans[1] = i
        return ans

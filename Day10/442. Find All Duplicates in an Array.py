class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
          ans=[]
          counts=Counter(nums)
          for i,j in counts.items():
               if j==2:
                  ans.append(i)
          return ans
        

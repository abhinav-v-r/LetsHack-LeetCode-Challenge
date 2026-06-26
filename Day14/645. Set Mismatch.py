class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        real_sum=(n*(n+1))//2
        need_sum=sum(set(nums))
        actual_sum=sum(nums)
        return [actual_sum-need_sum,real_sum-need_sum]
                
        

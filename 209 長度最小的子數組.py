class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        r,l = 0,0
        max_l = len(nums)
        while r < max_l:
            
        return min_len if min_len != float('inf') else 0
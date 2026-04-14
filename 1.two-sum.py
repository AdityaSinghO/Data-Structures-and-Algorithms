#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
          comp = target - n
          if comp in seen: return [seen[comp], i]
          seen[n] = i
        
# @lc code=end


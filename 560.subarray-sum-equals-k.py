#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count = prefix = 0
        seen = defaultdict(int); seen[0] = 1
        for n in nums:
          prefix += n
          count += seen[prefix - k]
          seen[prefix] += 1
        return count
        
# @lc code=end


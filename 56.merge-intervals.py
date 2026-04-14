#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
          if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
          else:
            merged.append([start, end])
        return merged
        
# @lc code=end


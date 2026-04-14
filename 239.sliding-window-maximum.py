#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq, res = deque(), []
        for i, n in enumerate(nums):
          while dq and nums[dq[-1]] < n: dq.pop()
          dq.append(i)
          if dq[0] == i - k: dq.popleft()
          if i >= k - 1: res.append(nums[dq[0]])
        return res
        
# @lc code=end


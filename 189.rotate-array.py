#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
# @lc code=end


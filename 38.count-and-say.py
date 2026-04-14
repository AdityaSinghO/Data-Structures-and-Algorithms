#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
           new, i = "", 0
           while i < len(result):
            cnt = 1
            while i+cnt < len(result) and result[i+cnt] == result[i]:
                cnt += 1
            new += str(cnt) + result[i]
            i += cnt
           result = new
        return result
        
# @lc code=end


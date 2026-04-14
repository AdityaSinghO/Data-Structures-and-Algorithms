#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need, missing = Counter(t), len(t)
        i = start = end = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not end or j - i < end - start:
                    start, end = i, j
        return s[start:end]
        
# @lc code=end


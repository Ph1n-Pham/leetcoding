'''
https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # base cases
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # memoization
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:   # if length of word fits in s and match w
                    dp[i] = dp[i + len(w)]
                if dp[i]:   # if matched, then no need to check other words
                    break
        return dp[0]


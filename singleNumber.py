'''
https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150

USING XOR
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

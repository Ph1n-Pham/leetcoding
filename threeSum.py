'''
https://leetcode.com/problems/3sum/description/
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = v + nums[l] + nums[r]    # same as 2 sum approach
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    # update left pointer
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

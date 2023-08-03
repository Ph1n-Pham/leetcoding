"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Check if the input list is empty
        if nums == []:
            return []
        
        # Initialize the list to store the summary ranges
        ranges = []
        
        # Initialize variables for the start and end of the range
        start = nums[0]
        end = nums[0]

        # Iterate through the numbers starting from the second element
        for num in nums[1:]:
            if num == end + 1:
                # The number is consecutive, update the end of the range
                end = num
            else:
                # The number is not consecutive, add the current range to the result list
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                
                # Reset the start and end to the current number
                start = num
                end = num

        # Add the last range to the result list
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")
        
        return ranges

# Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1s in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        cur_len = 0
        nums.append(0)
        for i in nums:
            if i == 1:
                cur_len += 1
            else:
                if max_len < cur_len:
                    max_len = cur_len
                cur_len = 0
        return max_len

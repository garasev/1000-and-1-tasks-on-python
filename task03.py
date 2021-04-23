# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for _ in nums]
        l = 0
        r = len(nums) - 1
        cur = r
        while True:
            if abs(nums[r]) > abs(nums[l]):
                res[cur] = nums[r]**2
                r -= 1
            else:
                res[cur] = nums[l]**2
                l += 1
            cur -= 1
            if cur == -1:
                break
        return res

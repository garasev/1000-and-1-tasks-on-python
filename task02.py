# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            tmp = 0
            while i >= 1:
                tmp += 1
                i /= 10
            if tmp % 2 == 0:
                res += 1
        return res

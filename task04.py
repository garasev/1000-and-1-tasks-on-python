# Duplicate Zeros
# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        tmp = 0
        l =  len(arr) - 1
        for i in range(l + 1):
            if i + tmp > l:
                break
            
            if arr[i] == 0:
                if i == l - tmp:
                    arr[l] = 0
                    l -= 1
                    break
                tmp += 1

        last = l - tmp

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + tmp] = 0
                tmp -= 1
                arr[i + tmp] = 0
            else:
                arr[i + tmp] = arr[i]

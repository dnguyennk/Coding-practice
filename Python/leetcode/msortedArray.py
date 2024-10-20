from ast import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set p1 and p2 to point to the end of their respective array
        p1 = m - 1
        p2 = n - 1 

        #Move p (m+n-1) backward through array, each time write the smallest values pointed at p1 or p2
        for p in range (m+n-1, -1, -1):
            if p2 < 0 :
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
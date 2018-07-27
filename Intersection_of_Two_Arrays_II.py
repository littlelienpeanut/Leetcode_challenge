from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        d = Counter(nums1)
        for n in nums2:
            if n in d and d[n] != 0:
                output.append(n)
                d[n] -= 1

        return output
        

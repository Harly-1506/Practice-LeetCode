class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        out_array = nums1 + nums2
        out_array.sort()
        
        if len(out_array) % 2 == 0:
            
            median = (out_array[int(len(out_array)/2 - 1)] + out_array[int(len(out_array)/2)] )/2
            
        else:
            m = int((len(out_array)+1)/2 - 1)
            median = out_array[m]
        
        return median
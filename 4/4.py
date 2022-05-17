class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_array = nums1 + nums2
        combined_array.sort()
        len_array = len(combined_array)
        
        if len_array == 1:
            return combined_array[0]
        
        # Odd
        if len_array % 2:
             return combined_array[len_array // 2]
        # Even
        else:
            upper_mid = len_array // 2
            return (combined_array[upper_mid - 1] + combined_array[upper_mid])/2
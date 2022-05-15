class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        
        diff = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                diff += 1
                
        return diff
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_area = 0
        while i < j:
            min_height = min(heights[i], heights[j])
            length = j - i
            area = min_height*length
            if area > max_area:
                max_area = area
            
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] <= heights[j]:
                i += 1
        
        return max_area
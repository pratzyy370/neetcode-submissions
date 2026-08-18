class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_size=0
        while left<right:
            width=right-left
            minimum=min(heights[left],heights[right])
            area=width * minimum
            max_size = max(max_size, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return max_size








        
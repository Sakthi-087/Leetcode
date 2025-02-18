class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        max_area = 0
        mini = 0
        while left < right:
            if height[left]<height[right]:
                mini = height[left]
            else:
                mini = height[right]
            area = (right-left) * mini

            if max_area < area:
                max_area = area
                
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_area
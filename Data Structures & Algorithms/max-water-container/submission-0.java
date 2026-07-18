class Solution {
    public int maxArea(int[] heights) {
        int maxValue = 0;
        int l = 0;
        int r = heights.length - 1;
        while(l<r){
            int temp = (r-l) * Math.min(heights[l], heights[r]);
            if(maxValue < temp){
                maxValue = temp;
            }

            if(heights[l] < heights[r]){
                l++;
            } else{
                r--;
            }
        }
        return maxValue;
    }
}

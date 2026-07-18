class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int i = 0;
        
        while(i < nums.length -1){
            if (i > 0 && nums[i] == nums[i-1]){
                i++;
                continue;
            }
            int j = nums.length -1;
            int k = i + 1;
            while(k<j){
                int threeSum = nums[i] + nums[k] + nums[j];
                if (threeSum< 0){
                    k++;
                } else if(threeSum > 0){
                    j--;
                } else{
                    result.add(Arrays.asList(nums[i] , nums[k] , nums[j]));
                    k++;
                    while(k<j && nums[k] == nums[k-1]){
                        k++;
                    }
                }
            }
            i++;
        }
        return result;
    }
}
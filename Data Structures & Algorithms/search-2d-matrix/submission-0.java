class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int columns = matrix[0].length;
        int first_r = 0;
        int last_r = rows - 1;
        while(first_r <= last_r){
            int first_c = 0;
            int last_c = columns - 1;
            int mid_l = first_r + (last_r - first_r) / 2;
            int[] arr = matrix[mid_l];
            if(target <= arr[last_c]){
                if(target >= arr[first_c]){
                    while(first_c <= last_c){
                        int mid = first_c + (last_c-first_c) / 2;
                        if(target == arr[mid]){
                            return true;
                        } else if(target < arr[mid]){
                            last_c = mid - 1;
                        } else{
                            first_c = mid + 1;
                        }
                    }
                    return false;
                } else {
                    last_r = mid_l - 1;
                }
            } else{
                first_r = mid_l + 1;
            }
        }
        return false;        
    }
}
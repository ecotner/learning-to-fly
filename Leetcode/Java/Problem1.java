import java.util.Arrays;

class Problem1{

    public static int[] Problem1(int[] nums, int target) {
        
        int[] ans = new int[2];
        boolean done = false;
        
        for (int i=0; i<nums.length; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    ans[0] = i; ans[1] = j;
                    done = true;
                    break;
                }
            }
            if(done){
                break;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        
        // convert args[0] to integer array
        String nums_str = args[0].substring(1, args[0].length()-1);
        String[] nums_str_array = nums_str.split(",");
        int[] nums = new int[nums_str_array.length];
        for(int i=0; i<nums.length; i++){
            nums[i] = Integer.parseInt(nums_str_array[i]);
        }

        int target = Integer.parseInt(args[1]);
        
        System.out.println(Arrays.toString(Problem1(nums, target)));
    }
}

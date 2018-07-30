class Solution {
    public int reverse(int x) {
        // Check to see if integer is negative, change to positive and set negative flag
        boolean is_neg = false;
        if(x < 0){
            x = (-1)*x;
            is_neg = true;
        }
        
        // Convert positive integer to string
        String str = new Integer(x).toString();
        
        // Reverse string
        StringBuilder builder = new StringBuilder(str);
        str = builder.reverse().toString();
        
        // Convert string back to int
        int y;
        try{
            y = Integer.parseInt(str);
        // If reversed int overflows, set y=0
        } catch(NumberFormatException e){
            y = 0;
        }
        
        // Multiply by -1 if original integer is negative
        if(is_neg){
            y = (-1)*y;
        }
        
        return y;        
    }
}

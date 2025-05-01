class Solution {
    public int hammingWeight(int n) {
        
        int ans = 0;
        while (n>0){
            int x = n>>1;
            if ((n-x)!=x){
                ans+=1;
            }
            n = x;
        }
        return ans;


    }
}
class Solution {


    public boolean doesItShip(int[] weights, int days, int cap){
        
        int currSum = 0;
        int i = 0;
        int d = 1;
        while (i<weights.length){
            if (currSum+weights[i]<=cap){
                currSum+=weights[i];
            }else{
                d+=1;
                currSum = weights[i];
            }
            if (d>days || weights[i]>cap){
                return false;
            }
            i+=1;
        }
        return true;
    }


    public int shipWithinDays(int[] weights, int days) {
        int lcap = 0;
        int rcap = 0;
        for (int w : weights) {
            rcap += w;
        }
        int test = 0;

        while (lcap<rcap){
            test = lcap+((rcap-lcap)/2);
            if (doesItShip(weights,days,test)){
                rcap = test;
            }else{
                lcap = test+1;
            }
        }

        return rcap;
    }
}
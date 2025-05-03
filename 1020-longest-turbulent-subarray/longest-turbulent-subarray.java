class Solution {
    public int maxTurbulenceSize(int[] arr) {
        
        /**
            2 5 1 52 53 24 2 92 24 254 12 52 52 91 142
        
             +1 -1 +1 +1 -1 -1 +1 -1 +1 -1 +1  2 +1 +1  
                0 0 2 0 -2 0 0 0 0 0 0 2
             longest subarray of +1 -1

             4 8 12 16
             +1 +1 +1

             9 4 2 10 7 8 8 1 9
             -1 -1 +1 -1 +1 2 -1 +1
             -2 3 2
             
         */

        if (arr.length==1){
            return 1;
        }

        boolean allequal =true;
        for (int i=0;i<arr.length-1;i+=1){
            if (arr[i]!=arr[i+1]){
                allequal=false;
            }
        }

        if (allequal){
            return 1;
        }


        for (int i=1;i<arr.length;i+=1){
            if (arr[i]>arr[i-1]){
                arr[i-1] = 1;
            }else if (arr[i]<arr[i-1]){
                arr[i-1] = -1;
            }else{
                arr[i-1] = 2;
            }
        }
        int longest0 = 1;
        int result = longest0;
        for (int i=0;i<arr.length-1;i+=1){
            if (arr[i+1]==2 || arr[i]==2){
                longest0 = 1;
                continue;
            }
            arr[i] = arr[i]+arr[i+1];
            if (arr[i]==0){
                longest0+=1;
            }else{
                longest0=1;
            }
            if (longest0>result){
                result = longest0;
            }
        }

        return result+1;


    }
}
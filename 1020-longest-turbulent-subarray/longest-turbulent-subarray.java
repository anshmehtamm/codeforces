class Solution {
    public int maxTurbulenceSize(int[] arr) {
        
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
                arr[i-1] = 0;
            }
        }

        int longest0 = 1;
        int result = longest0;
        for (int i=0;i<arr.length-1;i+=1){

            if (arr[i]==0){
                longest0 = 1;
                continue;
            }

            if (arr[i]+arr[i+1]==0){
                longest0+=1;
            }else{
                longest0=1;
            }

            result = Math.max(result, longest0);
        }


        return result+1;


    }
}
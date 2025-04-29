class Solution {
    public String minRemoveToMakeValid(String s) {
        

        int ans = 0;
        int sC = 0;
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c== '('){
                sC+=1;
                res.append(c);
            }else if (c==')'){
                if (sC>0){
                    sC-=1;
                    res.append(c);
                }else{
                   ans+=1;
                }
            }else{
                res.append(c);
            }
        }
        String r = res.toString();
        
        if (sC>0){
            StringBuilder res2 = new StringBuilder();
            // remove extra (
            for (int i = r.length()-1; i >=0 ; i--) {
                char c = r.charAt(i);
                if (c=='(' && sC>0){
                    sC-=1;
                    continue;
                }
                res2.append(c);
            }
            return res2.reverse().toString();
        }

        return res.toString();
        



    }
}
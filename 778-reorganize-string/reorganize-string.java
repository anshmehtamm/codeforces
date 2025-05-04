class Solution {
    public String reorganizeString(String s) {
        
        /**
        
            "[X1][X2][XN]"

            total characters 5 
            each character count a:3,b:2,c:22,d:15

            for each pair we need two distinct chars
            <ab><ab>

            dadadadbdbdcdcdcdcdcdcdcdcdc
            a3, b2, c11 d14
            d3,a3,b2c1

            dcdcdcdcdcdcdcdcdcdcdcadadad
            aabbcc
            aca
         */

        Map<Character, Integer> mp = new HashMap<>();

        for(int i=0;i<s.length();i+=1){
            char c = s.charAt(i);
            mp.put(c,mp.getOrDefault(c,0)-1);
        }

        Queue<Pair<Integer, Character>> pq = new PriorityQueue<>(Comparator.comparingInt(Pair::getKey));
        
        for (Character c: mp.keySet()){
            Pair<Integer, Character> p = new Pair(mp.get(c),c);
            pq.add(p);
        }

        StringBuilder result = new StringBuilder();

        while (pq.size()>1){
            Pair<Integer,Character> p1 = pq.poll();
            Pair<Integer,Character> p2 = pq.poll();
           
            result.append(p1.getValue());
            result.append(p2.getValue());
            
            if (p1.getKey()+1<0){
                pq.offer(new Pair(p1.getKey()+1, p1.getValue()));
            }
            if (p2.getKey()+1<0){
                pq.offer(new Pair(p2.getKey()+1, p2.getValue()));
            }
        }


        Pair<Integer,Character> last = pq.poll();
        if (last !=null && -last.getKey()>1){
            return "";
        }else if (last!=null && -last.getKey()==1)
            result.append(last.getValue());

        return result.toString();



    }
}
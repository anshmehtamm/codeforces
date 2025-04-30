class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {

        /**
            for each function (start) 
                - top of call stack function
                - next event time 
                - prev event time
                we add next_event_time
         */ 
        
        Stack<Integer> stack = new Stack<>();
        int currTime=0;
        int prevTime=0;
        int prevFuncId = -1;
        int[] times = new int[n];
        
        Arrays.fill(times,0);

        for (String log: logs){
            int extra = 0;
            String[] parts = log.split(":");
            int funcId = Integer.parseInt(parts[0]);
            String type = parts[1];
            currTime = Integer.parseInt(parts[2]);
            // calculate time for current on top of stack
            if (!stack.isEmpty()){
                if (type.equals("end")){
                    extra = 1;
                }
                times[stack.peek()] += (currTime - prevTime+extra);
            }
            if (type.equals("end")){
                prevTime = currTime+1;
            }else{
                prevTime = currTime;
            }
            // push
            if (type.equals("start")){
                stack.push(funcId);
                prevFuncId = funcId;
            }else{
                stack.pop();
            }
            System.out.println(times[0]);
        }

        return times;

        

    }
}
// https://programmers.co.kr/learn/courses/30/lessons/12910

import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> n = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor == 0)
                n.add(arr[i]);
        }
        int[] answer = {-1};
        if(n.size()==0){
            return answer;
        }else{
            answer = new int[n.size()];
            for (int i = 0; i < answer.length; i++) {
                answer[i] = n.get(i);
            }
            Arrays.sort(answer);
        }
        return answer;
    }
}
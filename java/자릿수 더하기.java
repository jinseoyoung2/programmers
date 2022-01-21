// https://programmers.co.kr/learn/courses/30/lessons/12931?language=java
// https://dda0e.tistory.com/68

import java.util.*;
public class Solution {
    public int solution(int n) {
        int answer = 0;
        String[] N = (""+n).split("");
        for(int i=0; i<N.length; i++){
            answer+=Integer.valueOf(N[i]);
        }
        return answer;
    }
}

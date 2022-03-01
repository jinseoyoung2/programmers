import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        for(int i = 0; i < strings.length; i++) { 
            answer[i] = strings[i].charAt(n)+strings[i];
        }
        Arrays.sort(answer);
        String[] arrList = new String[strings.length];
        for (int i = 0; i < answer.length; i++) {
            arrList[i] = answer[i].substring(1, answer[i].length());
        }
        return arrList;
    }
}
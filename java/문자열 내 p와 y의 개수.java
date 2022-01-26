// https://programmers.co.kr/learn/courses/30/lessons/12916?language=java

class Solution {
    boolean solution(String s) {
        int p=0, y=0;
        s = s.toLowerCase();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='p'){
                p++;
            }else if(s.charAt(i)=='y'){
                y++;
            }
        }
        boolean answer = p==y?true:false;
        return answer;
    }
}
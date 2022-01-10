# https://programmers.co.kr/learn/courses/30/lessons/12922?language=java

class Solution {
    public String solution(int n) {
        String answer = "";
        if(n%2==0){
            answer="수박".repeat(n/2);
        }else{
            answer="수박".repeat(n/2)+"수";
        }
        return answer;
    }
}

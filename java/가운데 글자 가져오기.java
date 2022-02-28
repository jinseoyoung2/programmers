// https://programmers.co.kr/learn/courses/30/lessons/12903?language=java

class Solution {
    public String solution(String s) {
        String[] N = s.split("");
        if(N.length%2==0){
            return (N[N.length/2-1]+N[N.length/2]);
        }else{
            return N[N.length/2];
        }
        
    }
}

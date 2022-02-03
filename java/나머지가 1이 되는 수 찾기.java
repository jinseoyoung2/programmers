// https://programmers.co.kr/learn/courses/30/lessons/87389?language=java
// https://dda0e.tistory.com/96

class Solution {
    public int solution(int n) {
        for(int i=1; i<n; i++){
            if(n%i==1){
                return i;
            }
        }
        return 0;
    }
}

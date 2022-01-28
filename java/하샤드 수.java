// https://programmers.co.kr/learn/courses/30/lessons/12947
// https://dda0e.tistory.com/86

class Solution {
    public boolean solution(int x) {
        String[] y = String.valueOf(x).split("");
        int z = 0;
        for(int i=0;i<y.length;i++){
            z+=Integer.parseInt(y[i]);
        }
        if(x%z==0){
            return true;
        }else{
            return false;
        }
    }
}

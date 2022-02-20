// https://programmers.co.kr/learn/courses/30/lessons/86051

import java.util.stream.IntStream;
class Solution {
    public int solution(int[] numbers) {
        int answer = 45 - IntStream.of(numbers).sum();
        return answer;
    }
}
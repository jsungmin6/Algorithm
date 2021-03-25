package com.programmers;

public class 내적 {
    public static void main(String[] args) {

        class Solution {
            public int solution(int[] a, int[] b) {
                int answer = 1234567890;
                int total = 0;
                for (int i = 0; i < a.length; i++) {
                    total += a[i]*b[i];
                }
                return total;
            }
        }

        int[] a = {1, 2, 3, 4};
        int[] b = {-3,-1,0,2};
        Solution solution = new Solution();
        System.out.println(solution.solution(a,b));
    }
}

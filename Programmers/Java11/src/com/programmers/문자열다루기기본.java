package com.programmers;

public class 문자열다루기기본 {
    class Solution {
        public boolean solution(String s) {
            boolean answer = true;

            if(s.length() != 4 && s.length() !=6){
                return false;
            }

            for(int i=0; i<s.length(); i++){
                if (!Character.isDigit(s.charAt(i))){
                    answer = false;
                    break;
                }
            }

            return answer;
        }
    }

}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;

public class 신규아이디추천 {
    static class Solution {
        public String solution(String new_id) {
            String answer = "";

            //모두 소문자로로
            String s1 = new_id.toLowerCase();

            //2단계 문자제거
            String s2 = "";
            for (int i = 0; i < s1.length(); i++) {
                char c = s1.charAt(i);
                if (!Character.isLowerCase(c) && !Character.isDigit(c) && c!='.' && c!='_' && c!='-'){
                    continue;
                } else {
                    s2 = s2 + c;
                }
            }

            //3단계 .. => .
            while (s2.contains("..")){
                s2 = s2.replace("..", ".");
            }

            answer = s2;

            //4단계
            if(s2.startsWith(".")){
                answer = answer.substring(1, answer.length());
            }

            if (answer.endsWith(".")) {
                answer = answer.substring(0, answer.length()-1);
            }

            //5단계
            if (answer.equals("")) {
                answer = "a";
            }

            //6단계
            if (answer.length() >= 16) {
                answer = answer.substring(0, 15);
            }

            if (answer.endsWith(".")) {
                answer = answer.substring(0, answer.length()-1);
            }

            //7단계

            if (answer.length() <= 2) {
                char c = answer.charAt(answer.length() - 1);
                while(answer.length() != 3){
                    answer = answer + c;
                }
            }

            return answer;


        }
    }

    public static void main(String[] args) {

        String new_id = "abcdefghijklmn.p";

        신규아이디추천.Solution solution = new 신규아이디추천.Solution();

        System.out.println(solution.solution(new_id));
    }

}

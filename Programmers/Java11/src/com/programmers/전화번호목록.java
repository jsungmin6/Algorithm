import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class 전화번호목록 {
    static class Solution {
        public boolean solution(String[] phone_book) {
            for (int i = 0; i < phone_book.length; i++) {
                for (int j = i+1; j < phone_book.length; j++) {
                    if(phone_book[j].startsWith(phone_book[i])) return false;
                    if(phone_book[i].startsWith(phone_book[j])) return false;
                }
            }

            return true;
        }
    }

    public static void main(String[] args) {

        String[] phone_book = {"12","123","1235","567","88"};

        전화번호목록.Solution solution = new 전화번호목록.Solution();
        boolean solution1 = solution.solution(phone_book);
        System.out.println(solution1);

    }
}

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 주식가격 {
    static class Solution {
        public int[] solution(int[] prices) {
            ArrayList<Integer> li = new ArrayList<>();
            int[] answer = {};

            for (int i = 0; i < prices.length; i++) {
                int cnt=0;
                for (int j = i+1; j < prices.length; j++) {
                    cnt+=1;
                    if(prices[i] > prices[j]){
                        li.add(cnt);
                        break;
                    }

                    if(j == prices.length-1){
                        li.add(cnt);
                        break;
                    }
                }
            }

            li.add(0);

            answer = new int[li.size()];

            for (int i = 0; i < answer.length; i++) {
                answer[i] = li.get(i);
            }

            return answer;
        }
    }

    public static void main(String[] args) {

        int[] prices = {1, 2, 3, 2, 3};

        주식가격.Solution solution = new 주식가격.Solution();

        int[] solution1 = solution.solution(prices);
        for (int i : solution1) {
            System.out.println(i);
        }
    }
}

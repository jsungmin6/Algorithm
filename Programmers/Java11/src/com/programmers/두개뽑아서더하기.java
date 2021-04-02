import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;

public class 두개뽑아서더하기 {

    static class Solution {
        public int[] solution(int[] numbers) {
            int[] answer = {};
            HashSet<Integer> set1 = new HashSet<Integer>();
            for (int i = 0; i < numbers.length; i++) {
                for (int j = i+1; j < numbers.length; j++) {
                    set1.add(numbers[i] + numbers[j]);
                }
            }

            System.out.println("set1 :"+set1);
            ArrayList<Integer> result = new ArrayList<>();

            Iterator<Integer> iterator = set1.iterator();
            while (iterator.hasNext()) {
                result.add(iterator.next());
            }



            System.out.println("result :"+result);


            answer = new int[result.size()];

            for (int i = 0; i < answer.length; i++) {
                answer[i] = result.get(i);
            }

            Arrays.sort(answer);


            return answer;
            }

        }

    public static void main(String[] args) {

        int[] numbers = {2, 1, 3, 4, 1};

        Solution solution = new Solution();

        int[] solution1 = solution.solution(numbers);

        for (int i : solution1) {
            System.out.println(i);
        }
    }

    }

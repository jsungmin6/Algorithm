import java.util.*;

public class 실패율 {
    static class Solution {
        public int[] solution(int N, int[] stages) {

            List<Stage> lastStages = new ArrayList<>();
            int total = stages.length;

            for (int i = 1; i < N+1; i++) {
                double cnt = 0;
                for (int j = 0; j < stages.length; j++) {
                    if (stages[j] == i) {
                        cnt+=1;
                    }
                }
                Double failRate = cnt / total;
                total -= cnt;

                Stage s = new Stage(i, failRate);
                lastStages.add(s);
            }

            Collections.sort(lastStages);


            int[] answer = new int[N];
            for (int i = 0; i < N; i++) {
                answer[i] = lastStages.get(i).id;
            }

            return answer;
        }

        class Stage implements Comparable<Stage> {
            public int id;
            public double failure;

            public Stage(int id_, double failure_) {
                id = id_;
                failure = failure_;
            }

            @Override
            public int compareTo(Stage o) {
                if (failure < o.failure ) {
                    return 1;
                }
                if (failure > o.failure ) {
                    return -1;
                }
                return 0;
            }
        }

    }

    public static void main(String[] args) {

        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
        int N = 5;

        실패율.Solution solution = new 실패율.Solution();

        int[] solution1 = solution.solution(N, stages);
        for (int i : solution1) {
            System.out.println(i);
        }
    }
}

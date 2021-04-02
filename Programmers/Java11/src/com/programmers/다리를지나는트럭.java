import java.util.LinkedList;
import java.util.Queue;

public class 다리를지나는트럭 {
    static class Solution {
        public int solution(int bridge_length, int weight, int[] truck_weights) {

            int bridge_weight = 0;
            int answer = 0;
            Queue<Integer> queue = new LinkedList<>();
            for (int i = 0; i < bridge_length; i++) {
                queue.add(0);
            }


            System.out.println("q : "+queue);
            for (int i = 0; i < truck_weights.length; i++) {
                if(bridge_weight+truck_weights[i] <= weight){
                    bridge_weight-= queue.poll();
                    queue.add(truck_weights[i]);
                    bridge_weight+=truck_weights[i];
                    answer+=1;
//                    System.out.println("q : "+queue);
                } else {
                    while(bridge_weight+truck_weights[i] > weight){
                        bridge_weight-= queue.poll();
                        if(bridge_weight+truck_weights[i] > weight){
                            queue.add(0);
                        }
                        answer+=1;
//                        System.out.println("while q : "+queue);
                    }
                    queue.add(truck_weights[i]);
                    bridge_weight+=truck_weights[i];
//                    System.out.println("q : "+queue);
                }
            }

            //다리비우기

            answer+=bridge_length;

            return answer;
        }
    }

    public static void main(String[] args) {

        int bridge_length = 5;
        int weight = 5;
        int[] truck_weights = {2, 2, 2, 2, 1, 1, 1, 1, 1};

        다리를지나는트럭.Solution solution = new 다리를지나는트럭.Solution();

        System.out.println(solution.solution(bridge_length,weight,truck_weights));
    }
}

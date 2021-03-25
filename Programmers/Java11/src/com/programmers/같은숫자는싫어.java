package com.programmers;

import java.util.ArrayList;

public class 같은숫자는싫어 {
    public static void main(String[] args) {
        class Solution {
            public int[] solution(int []arr) {
                int[] answer = {};

                ArrayList<Integer> li = new ArrayList<>();

                for(int i=0; i<arr.length; i++){

                    if(li.isEmpty()){
                        li.add(arr[i]);
                    }
                    else if(li.get(li.size()-1) != arr[i]){
                        li.add(arr[i]);
                    }
                    else continue;
                }

                System.out.println("li : "+li);

                answer = new int[li.size()];

                for (int i = 0; i < li.size(); i++) {
                    answer[i] = li.get(i);
                }

                for (int i : answer) {
                    System.out.println(i);
                }

                return answer;
            }
        }

        int[] arr = {1,1,3,3,0,1,1};
        Solution solution = new Solution();
        solution.solution(arr);


    }
}

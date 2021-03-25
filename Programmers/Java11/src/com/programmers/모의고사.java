package com.programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static java.lang.Math.max;

public class 모의고사 {
    public static void main(String[] args) {
        class Solution {
            public int[] solution(int[] answers) {
                int[] answer = {};
                List<Integer> arrList = new ArrayList<>();
                int[] s1 = {1, 2, 3, 4, 5};
                int[] s2 = {2, 1, 2, 3, 2, 4, 2, 5};
                int[] s3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

                int solveS1 = 0; int solveS2 = 0; int solveS3 = 0;

                for(int i=0; i<answers.length; i++){
                    int idx1 = i%5; int idx2 = i%8; int idx3 = i%10;
                    if(s1[idx1] == answers[i]){
                        solveS1+=1;
                    }
                    if(s2[idx2] == answers[i]){
                        solveS2+=1;
                    }
                    if(s3[idx3] == answers[i]){
                        solveS3+=1;
                    }
                }
                List<Integer> li = List.of(solveS1, solveS2, solveS3);

                Integer max = Collections.max(li);
                int k=1;
                for (Integer i : li) {
                    if(i == max){
                        arrList.add(k);
                    }
                    k++;
                }
                answer = new int[arrList.size()];
                for (int i = 0; i < arrList.size(); i++) {
                    answer[i] = arrList.get(i);
                }

                return answer;
            }
        }


        int[] answers = {1,2,3,4,5};
        Solution solution = new Solution();
        System.out.println(solution.solution(answers));

    }
}

class Solution {
    public static int[] solution(int[] answers) {
        int[][] patterns = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };

        int[] hit = new int[3];
        for(int i = 0; i < hit.length; i++) {
            for(int j = 0; j < answers.length; j++) {
                if(patterns[i][j % patterns[i].length] == answers[j]) hit[i]++;
            }
        }

        int max = Math.max(hit[0], Math.max(hit[1], hit[2]));
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < hit.length; i++)
            if(max == hit[i]) list.add(i + 1);

        int[] answer = new int[list.size()];
        int cnt = 0;
        for(int num : list)
            answer[cnt++] = num;
        return answer;
    }
}



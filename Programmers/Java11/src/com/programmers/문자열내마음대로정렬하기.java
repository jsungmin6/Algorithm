package com.programmers;

import java.util.ArrayList;
import java.util.Collections;

public class 문자열내마음대로정렬하기 {


    public static void main(String[] args) {
        class Solution {
            public String[] solution(String[] strings, int n) {
                String[] answer = {};
                ArrayList<String> arr = new ArrayList<>();
                for (int i = 0; i < strings.length; i++) {
                    arr.add("" + strings[i].charAt(n) + strings[i]);
                }
                Collections.sort(arr);
                answer = new String[arr.size()];
                for (int i = 0; i < arr.size(); i++) {
                    answer[i] = arr.get(i).substring(1, arr.get(i).length());
                }
                return answer;
            }
        }

        String[] strings = {"abce", "abcd", "cdx"};
        int n = 2;
        Solution solution = new Solution();
        String[] solution1 = solution.solution(strings, n);
        for (String s : solution1) {
            System.out.println(s);
        }
    }
}

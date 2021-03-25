package com.programmers;

import java.util.Arrays;

public class 소수찾기 {
    public static void main(String[] args) {
        class Solution {
            public int solution(int num) {
                int answer = 0;
//                boolean[] isPrime = new boolean[n+2];
//                Arrays.fill(isPrime,true);

                boolean[] arr = new boolean[num+1];    //true 이면 해당 인덱스 소수.
                arr[0] = arr[1] = false;
                for(int i=2; i<=num; i+=1) {
                    arr[i] = true;
                }

                //2 부터 숫자를 키워가며 배수들을 제외(false 할당)
                for(int i=2; i*i<=num; i+=1) {
                    for(int j=i*i; j<=num; j+=i) {
                        arr[j] = false;        //2를 제외한 2의 배수 false
                    }
                }
                for(int i=2; i<=num; i+=1) {
                    if(true == arr[i]) {
                        answer+=1;
                    }
                }
                return answer;
            }
        }

        class Solution2 {
            public int solution(int n) {
                int answer = 0;
                boolean[] isPrime = new boolean[n+1];
                Arrays.fill(isPrime,true);
                for(int i=2; i*i<n+1;i++){
                    for (int j = i*i; j < n+1; j+=i) {
                        isPrime[j] = false;
                    }
                }

                for(int i=2; i<n+1; i+=1) {
                    if(isPrime[i]) {
                        answer+=1;
                    }
                }
                return answer;
            }
        }

        int n = 10;

        Solution2 solution = new Solution2();
        System.out.println(solution.solution(n));

    }
}

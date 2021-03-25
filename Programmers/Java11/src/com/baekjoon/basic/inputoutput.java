package com.baekjoon.basic;
import java.util.*;
import java.io.*;

public class inputoutput {
    public static void main(String[] args) throws Exception {
        int a = 0;
        int b = 0;
        boolean Aflag = true;


        BufferedReader lineTemp = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = lineTemp.readLine().split(" ");
        a = Integer.parseInt(temp[0]);
        b = Integer.parseInt(temp[1]);
        System.out.println(Integer.toString(a+b));
    }
}

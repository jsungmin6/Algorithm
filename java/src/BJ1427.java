import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

public class BJ1427 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        Integer[] arr = new Integer[s.length()];

        for (int i = 0; i < s.length(); i++) {
            arr[i] = Integer.parseInt(String.valueOf(s.charAt(i)));
        }

        Arrays.sort(arr, Collections.reverseOrder());
        for (int i : arr) {
            System.out.print(i);
        }




    }

    public static void main2(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer>arr=new ArrayList<>();

        int cnt = Integer.parseInt(br.readLine());
        int ten=1;

        while(cnt/ten!=0) {
            int temp=cnt/ten;
            ten=ten*10;
            arr.add( temp%10);

        }
        Collections.sort(arr);

        Collections.reverse(arr);

        for (int i = 0; i < arr.size(); i++){
            System.out.print(arr.get(i));
        }
    }

    public static void main3(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        int l = str.length();

        int[] i_arr = new int[10];

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < l; i++) {
            String s = str.substring(i,i+1);

            i_arr[Integer.parseInt(s)]++;

        }
        for (int i = 9; i >= 0 ; i--) {

            for(int j=0; j < i_arr[i];j++) {
                sb.append(i);
            }

        }

        System.out.println(sb.toString());

    }

}

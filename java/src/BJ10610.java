import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class BJ10610 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] sList = br.readLine().split("");
        int l = sList.length;
        int[] nums = new int[l];
        int total = 0;

        boolean chZero = false;
        for (int i = 0; i < l; i++) {
            if(sList[i].equals("0")){
                chZero = true;
            }
            total += Integer.parseInt(sList[i]);
        }

        if(!chZero){
            System.out.println(-1);
        }
        else{
            if(total%3 != 0){
                System.out.println(-1);
            } else{
                Arrays.stream(sList).sorted(Comparator.reverseOrder())
                        .forEach(System.out::print);
            }

        }
    }

    public static void main2(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] c_arr = br.readLine().toCharArray();
        int sum = 0;
        Arrays.sort(c_arr);
        for (char c : c_arr) {
            sum += c - '0';
        }
        if (sum % 3 != 0 || c_arr[0] != '0') {
            System.out.println(-1);
        } else {
            StringBuilder sb = new StringBuilder(new String(c_arr));
            System.out.println(sb.reverse());
        }
    }
}


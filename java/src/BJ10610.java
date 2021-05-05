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
}

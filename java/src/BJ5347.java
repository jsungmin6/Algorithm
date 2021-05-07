import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ5347 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] sList = br.readLine().split(" ");
            int a = Integer.parseInt(sList[0]);
            int b = Integer.parseInt(sList[1]);

            long answer = Lcm(a, b);

            System.out.println(answer);

        }


    }

    private static long Lcm(int a, int b) {
        long big,small;

        if(a>b){
            big = a;
            small = b;
        } else{
            big = b;
            small = a;
        }

        long gcd = Gcd(big, small);
        long lcm = (big * small) / gcd;

        return lcm;
    }

    private static long Gcd(long big, long small) {

        if (big % small == 0) {
            return small;
        }
        return Gcd(small, big % small);

    }
}

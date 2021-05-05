import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ2875 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        int M = Integer.parseInt(s[1]);
        int K = Integer.parseInt(s[2]);

        for (int i = 0; i < K; i++) {
            if (N > 2 * M) {
                N -= 1;
            } else {
                M -= 1;
            }
        }

        if (N > 2 * M) {
            System.out.println(M);
        } else {
            System.out.println(N/2);
        }
    }
}

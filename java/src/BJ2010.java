import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ2010 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int total = 1;
        for (int i = 0; i < N; i++) {
            total += Integer.parseInt(br.readLine()) - 1;
        }

        System.out.println(total);


    }
}
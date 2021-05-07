import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ14652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] sList = br.readLine().split(" ");
        int N = Integer.parseInt(sList[0]);
        int K = Integer.parseInt(sList[1]);
        int M = Integer.parseInt(sList[2]);

        System.out.println(M / K + " " + M % K);

    }

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ2869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        long A = Long.parseLong(s[0]);
        long B = Long.parseLong(s[1]);
        long V = Long.parseLong(s[2]);
        long diff = A-B;
        long dest = V-A; // 여기까지 오면 마지막으로 A만큼 더하면 정답임
        long cnt = dest/diff;
        if(dest % diff != 0) {
            System.out.println(cnt+2);
        } else {
            System.out.println(cnt+1);
        }
    }
}

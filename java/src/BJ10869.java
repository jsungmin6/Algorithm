import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ10869 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] arr = br.readLine().split(" ");
        Integer a = Integer.parseInt(arr[0]);
        Integer b = Integer.parseInt(arr[1]);

        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);
    }
}

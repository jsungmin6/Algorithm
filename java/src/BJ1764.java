import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class BJ1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        int M = Integer.parseInt(s[1]);
        HashSet<String> noListen = new HashSet<>();
        HashSet<String> noLook = new HashSet<>();

        for (int i = 0; i < N; i++) {
            noListen.add(br.readLine());
        }

        for (int i = 0; i < M; i++) {
            noLook.add(br.readLine());
        }

        noListen.retainAll(noLook);

        System.out.println(noListen.size());
        noListen.stream()
                .sorted()
                .forEach(System.out::println);

    }
}

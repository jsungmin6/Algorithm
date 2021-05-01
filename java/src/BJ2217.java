import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class BJ2217 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> nums = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }

        List<Integer> result = nums.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());

        int answer = 0;

        for (int i = 1; i < N + 1; i++) {
            int max_w = i*result.get(i-1);
            if(max_w > answer){
                answer = max_w;
            }
        }
        System.out.println(answer);

    }
}

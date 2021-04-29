import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class BJ5576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> W = new ArrayList<>();
        List<Integer> K = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            W.add(Integer.parseInt(br.readLine()));
        }
        for (int i = 0; i < 10; i++) {
            K.add(Integer.parseInt(br.readLine()));
        }

        System.out.print(rank3(W) + " " +rank3(K));

    }

    public static int rank3(List<Integer> list){
        List<Integer> result = list.stream()
                .sorted(Comparator.reverseOrder())
                .limit(3)
                .collect(Collectors.toList());
        int total = 0;
        for (Integer i : result) {
            total +=i;
        }
        return total;
    }
}

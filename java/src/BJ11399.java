import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;
import java.util.function.Function;

public class BJ11399 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();
        String[] P = br.readLine().split(" ");

        List<Integer> int_list = map(P, (String s) -> Integer.parseInt(s));

        int_list.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1-o2;
            }
        });
        int answer = 0;
        int total = 0;
        for (int i = 0; i < int_list.size(); i++) {
            total += int_list.get(i);
            answer += total;
        }
        System.out.println(answer);


    }

    public static List<Integer> map(String[] list, Function<String,Integer> f) {
        List<Integer> result = new ArrayList<>();
        for (String s : list) {
            result.add(f.apply(s));
        }
        return result;
    }

    public static void main2(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//		String str = br.readLine();
//		StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[1001];

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            arr[x]++;
        }

        int sum = 0;
        int total = 0;

        for (int i = 0; i <= 1000; i++) {

            while (arr[i] != 0) {
                sum += i;
                total += sum;
                arr[i]--;
            }
        }

        bw.write(Integer.toString(total));
        bw.flush();
        bw.close();
        br.close();
    }
}

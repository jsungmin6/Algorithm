import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.List;

public class BJ12015 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] s = br.readLine().split(" ");
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        List<Integer> temp = new ArrayList<>();
        temp.add(0);

        for (int i : arr) {
            if(temp.get(temp.size()-1) < i){
                temp.add(i);
            }
            else{
                int idx = bisect(temp, i);
                temp.set(idx, i);
                System.out.println(temp.toString());
            }
        }

        System.out.println(temp.size()-1);

    }

    private static int bisect(List<Integer> temp, int i) {
        int lo = 0;
        int hi = temp.size()-1;
        int answer = 0;

        while(lo <= hi){
            int mid = (lo+hi)/2; // mid는 인덱스 위치이다.
            int result = temp.get(mid); // 인덱스에 해당하는 값이다. 이게 i보단 작거나 같아야 한다.
            if(result >= i){
                answer = mid;
                hi = mid -1;
            } else {
                //이건 원하는 인덱스가 절대 아님 왜냐면 result 가 i 보다 작음
                lo = mid +1;
            }
        }
        return answer;


    }
}

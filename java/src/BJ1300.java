import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ1300 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        long lo = 1;
        long hi = k;
        long answer = 0;
        while (lo <= hi) {
            long mid = (lo+hi)/2;

            long result = solve(N,mid);
//            System.out.println("lo,hi : "+lo+" "+hi);
//            System.out.println("mid,result : "+mid+" "+result);


            if(k <= result){
                answer = mid;
                hi = mid-1;
            } else {
                lo = mid+1;
            }
        }

        System.out.println(answer);

    }

    public static long solve(long N, long mid){
        long cnt = 0;
        for (int i = 1; i < N+1; i++) {
            long j = mid/i;
            if(j > N){
                cnt+=N;
            } else {
                cnt+=j;
            }
        }
        return cnt;
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class BJ7576 {

    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int answer = 0;

        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        int[][] mat = new int[N][M];
        Queue<int[]> q = new LinkedList<>();

        int zeroNum = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < M; j++) {
                mat[i][j] = Integer.parseInt(st.nextToken());

                if(mat[i][j] == 1){
                    q.add(new int[]{i, j});
                }
                if (mat[i][j] == 0) {
                    zeroNum+=1;
                }
            }
        }


        // bfs 진행
        while (!q.isEmpty()) {

            int qSize = q.size();
            answer+=1;
            for (int d = 0; d < qSize; d++) {
                int[] poll = q.poll();
                int x = poll[0];
                int y = poll[1];



                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx >= 0 && nx < N && ny >= 0 && ny < M && mat[nx][ny] != 1 && mat[nx][ny] != -1) {
                        mat[nx][ny] = 1;

                        q.add(new int[]{nx, ny});
                    }

                }
            }
        }

        //결과 확인
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (mat[i][j] == 0) {
                    answer = -1;
                    break;
                }
            }
            if (answer == -1) {
                break;
            }
        }
        if (zeroNum == 0) {
            System.out.println(0);
        } else if (answer == -1) {
            System.out.println(answer);
        } else {
            System.out.println(answer-1);
        }

    }
}

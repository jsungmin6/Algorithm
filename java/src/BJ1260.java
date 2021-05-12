import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BJ1260 {
    static int N;
    static int M;
    static int V;
    static boolean[] visit;
    static LinkedList<Integer>[] list;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        list = new LinkedList[N+1];
        visit = new boolean[N + 1];

        for (int i = 0; i <= N; i++) {
            list[i] = new LinkedList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            list[n1].add(n2);
            list[n2].add(n1);

        }

        for (int i = 0; i <= N; i++) {
            Collections.sort(list[i]);
        }
        dfs(V); sb.append("\n");
        visit = new boolean[N + 1];
        bfs(V);
        System.out.println(sb);



    }

    private static void dfs(int start) {
        if(visit[start]) return;

        visit[start] = true;
        sb.append(start).append(" ");
        for (int next : list[start]) {
            if (!visit[next]) {
                dfs(next);
            }
        }
    }

    private static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visit[start] = true;
        while(!q.isEmpty()){
            int x = q.poll();
            sb.append(x).append(" ");
            for (int next : list[x]) {
                if (!visit[next]) {
                    visit[next] = true;
                    q.add(next);
                }
            }
        }
    }
}

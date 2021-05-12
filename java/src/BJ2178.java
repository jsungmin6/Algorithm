import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Coor {
    int x;
    int y;
    int cost;
    public Coor(int x, int y, int cost){
        this.x = x;
        this.y = y;
        this.cost= cost;
    }
}

public class BJ2178 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int row = Integer.parseInt(st.nextToken());
        int col = Integer.parseInt(st.nextToken());

        int[][] inputMap = new int[row][col];

        for (int r = 0 ; r < row ; r++){
            String lineInput = br.readLine();
            for (int c = 0 ; c < col ; c++){
                inputMap[r][c] = lineInput.charAt(c) - '0';
            }
        }

        Queue<Coor> q = new LinkedList<Coor>();
        boolean[][] visited = new boolean[row][col];

        q.add(new Coor(0, 0, 1));
        visited[0][0] = true;

        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        while (!q.isEmpty()) {
            Coor tempCoor = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = tempCoor.x + dx[i];
                int ny = tempCoor.y + dy[i];

                if (tempCoor.x == row-1 && tempCoor.y == col-1){
                    System.out.println(tempCoor.cost);
                    break;
                }

                if( nx >=0 && nx <row && ny >= 0 && ny < col && !visited[nx][ny] && inputMap[nx][ny]==1){
                    q.add(new Coor(nx, ny, tempCoor.cost + 1));
                    visited[nx][ny] = true;
                }

            }

        }


    }
}

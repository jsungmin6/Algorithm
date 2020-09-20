import java.util.*;
public class test {
static final int INF=999999999;
static int F,S,G,U,D;
static boolean[] check=new boolean[1000001];
static int[] dp=new int[1000001];
static int go(int current) {
if (current<=0 || current>F) {
return INF;
}
if ((S-G>0&&D==0)||((S-G)<0&&U==0)) {
return INF;
}
if (current==S) {
check[S]=true;
dp[S]=0;
return 0;
}
if (check[current]==true) {
return dp[current];
}
check[current]=true;
dp[current]=Math.min(go(current-U), go(current+D))+1;
return dp[current];
}
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
F=sc.nextInt();
S=sc.nextInt();
G=sc.nextInt();
U=sc.nextInt();
D=sc.nextInt();
for (int i=0;i<=F;i++) {
check[i]=false;
dp[i]=INF;
}
int ans=go(G);
if (ans>=999999999) {
System.out.print("use the stairs");
}else {
System.out.println(ans);
}
}
}

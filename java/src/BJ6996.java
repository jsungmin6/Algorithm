import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ6996 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            String[] words = br.readLine().split(" ");
            boolean answer = Match(words[0], words[1]);
            if(answer){
                System.out.println(words[0] + " & " + words[1] + " are anagrams.");
            } else {
                System.out.println(words[0] + " & " + words[1] + " are NOT anagrams.");
            }
        }
    }

    public static boolean Match(String a, String b) {
        if (SortString(a).equals(SortString(b))) {
            return true;
        }
        return false;
    }

    public static String SortString(String a){
        char[] StringtoChar1 = a.toCharArray();
        Arrays.sort(StringtoChar1);
        return new String(StringtoChar1);
    }
}

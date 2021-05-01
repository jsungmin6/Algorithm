import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class BJ10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Member> members = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            members.add(new Member(Integer.parseInt(s[0]),s[1]));
        }

        members.stream()
                .sorted(Comparator.comparing(Member::getAge))
                .forEach(member -> System.out.println(member.getAge() + " " + member.getName()));

    }

    public static class Member{
        public int age;
        public String name;

        public Member(int age, String name) {
            this.age = age;
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }



}

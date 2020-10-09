import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

	Scanner sc = new Scanner(System.in);

	int cnt_number = sc.nextInt();  // 배열 원소의 갯수

	int start = 1;
	int end = 1;
	int cnt =0; // 경우의 수

	while(end<=cnt_number) {
	int total =0;
	if(start== 1) {
		total = partial_sum(end);
	}else {
		total = partial_sum(end)-partial_sum(start-1);
	}

	if (total<cnt_number) {
		end++;
	}else if (total>cnt_number) {
		start++;
	}else if(total == cnt_number) {
		cnt++;
		start++;
		end++;
	}
	}

	System.out.println(cnt);




	}


	static int partial_sum(int a) {
		return (1+a)*a/2;
	}



}

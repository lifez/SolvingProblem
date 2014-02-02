import java.util.Scanner;
class main{
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int x = in.nextInt();
		if (x%2==0){
			if(x==2){
				System.out.print("NO");
			}
			else{
				System.out.print("YES");
			}
		}
		else{
			System.out.print("NO");
		}
	}
}
import java.util.Scanner;
class team{
	public static int chk(int[] ans,int k){
		int i,n=0;
		for(i=0;i<3;i++){
			if(ans[i]==1){
				n++;
			}
		}
		return n;
	}
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int i,n,problem=0;
		int[] ans = new int[100];
		n = in.nextInt();
		for(i=0;i<n;i++){
			ans[0] = in.nextInt();
			ans[1] = in.nextInt();
			ans[2] = in.nextInt();
			if(chk(ans,n)>1){
				problem++;
			}
		}
		System.out.print(problem);
	}
}
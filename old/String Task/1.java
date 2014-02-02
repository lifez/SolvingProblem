import java.util.Scanner;
class stringtask{
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		String x;
		char[] S = new char[100];
		int i;
		x = in.next();
		x = x.toLowerCase();
		S = x.toCharArray();
		for(i = 0;i<S.length;i++){
			if(S[i]=='a'||S[i]=='e'||S[i]=='i'||S[i]=='o'||S[i]=='u'||S[i]=='y'){
				System.out.format("");
			}
			else{
				System.out.format(".%c",S[i]);
			}
		}
		
	}
}
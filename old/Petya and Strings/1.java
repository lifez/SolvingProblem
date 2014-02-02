import java.util.Scanner;
class petyaandstrings{
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		String x,y;
		x = in.nextLine();
		y = in.nextLine();
		x = x.toUpperCase();
		y = y.toUpperCase();
		int compareResult = x.compareTo(y);
		if(compareResult>0) System.out.print(1);
		else if (compareResult==0) System.out.print(0);
		else System.out.print(-1);
	}
}
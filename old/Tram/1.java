import java.util.Scanner;
class tram{
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int x,cap=0,maxcap=0;
		int[] passen = new int[2];
		x = in.nextInt();
		while (x>0){
			passen[0] = in.nextInt();
			passen[1] = in.nextInt();
			cap-=passen[0];
			cap+=passen[1];
			if(cap>maxcap){
				maxcap=cap;
			}
			x--;
		}
		System.out.print(maxcap);
	}
	
}
import java.util.Scanner;
class doublecola{
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int x,y=5;
		x = in.nextInt();
		String[] Name= new String[] {"Sheldon","Leonard","Penny","Rajesh","Howard"};
		while(true){
			if(x<=y){
				y/=5;
				System.out.print(Name[(x-1)/y]);
				break;
			}
			else{
				x-=y;
				y*=2;
			}
		}

	}
}
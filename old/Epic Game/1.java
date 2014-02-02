import java.util.Scanner;
class epicgame{
	public static int gcd(int a,int b){
		int c=0;
		while (a!=0){
			c=a;
			a=b%a;
			b=c;
		}
		return b;
	}
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int x,y,z,point=0;
		x = in.nextInt();
		y = in.nextInt();
		z = in.nextInt();
		while(true){
			if(point==0){
				z-=gcd(x,z);
				if(z<=0){
					System.out.print("0");
					break;
				}
				point++;

			}
			if(point==1){
				z-=gcd(y,z);
				if(z<=0){
					System.out.print("1");
					break;
				}
				point--;
			}
		}

	}
}
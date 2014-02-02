import java.util.Scanner;
public class insomniacure{
	public static int chk_hit(int dod,int d,int[] dragon){
		int hit=0;
		while (d!=0){
			if (d%dod==0 && dragon[d-1]==1){
				hit++;
				dragon[d-1] = 0;
			}
			d--;
		}
		return hit;
	}
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int k,l,m,n,d,hit=0,i=0;
		int[] dragon = new int[100000];
		k = in.nextInt();
		l = in.nextInt();
		m = in.nextInt();
		n = in.nextInt();
		d = in.nextInt();
		for(i=0;i<d;i++){
			dragon[i]=1;
		}
		hit+=chk_hit(k,d,dragon);
		hit+=chk_hit(l,d,dragon);
		hit+=chk_hit(m,d,dragon);
		hit+=chk_hit(n,d,dragon);
		System.out.print(hit);

	}
}
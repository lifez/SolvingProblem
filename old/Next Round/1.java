import java.util.Scanner;
public class nextround{
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int limit,Smax,sum,i,j;
		int[] score = new int[100];
		i =0;
		sum = 0;
		j = 0;
		limit = in.nextInt();
		Smax = in.nextInt();
		while (limit>0){
			score[i] = in.nextInt();
			i++;
			limit--;
		}
		for(j=0;j<i;j++){
			if(score[j]>0 && score[j]>=score[Smax-1]){
				sum++;
			}
		}
		System.out.format("%d",sum);
	}
}
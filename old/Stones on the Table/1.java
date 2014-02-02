import java.util.Scanner;
import java.util.Collections;
class stoneonthetable{
	public static boolean all_equal(char[] array){
		int i=0,count=0;
	for(i=0;i<array.length-1;i++){
		if(array[i]==array[i+1]){
			count++;
		}
	}
	return count==array.length-1; 
	}
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int x,i=0,count=0;
		String stone;
		char[] instone = new char[50];
		x = in.nextInt();
		stone = in.next();
		instone = stone.toCharArray();
		for(i=0;i<x-1;i++){
			if (instone[i]==instone[i+1]) count++;
		}
		if (all_equal(instone)) count = x-1;
		System.out.print(count);

	}
}
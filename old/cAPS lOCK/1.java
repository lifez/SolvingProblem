import java.util.Scanner;
import java.lang.Character;

public class cAPSlOCK{
	public static int chk(String word){
		int i,n=0;
		char[] wordarray = word.toCharArray();
		for(i=0;i<word.length();i++){
			if(Character.isLowerCase(wordarray[i])){
				n++;
			}
		}
		return n;
	}
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		String word;
		int i;
		word = in.nextLine();
		char[] wordarray = word.toCharArray();
		if(Character.isLowerCase(wordarray[0]) && chk(word)>1){
			System.out.print(word);
		}
		else if(Character.isLowerCase(wordarray[0]) && chk(word)<=1){
			wordarray[0] = Character.toUpperCase(wordarray[0]);
			System.out.print(wordarray[0]);
			for(i=1;i<word.length();i++){
				wordarray[i] = Character.toLowerCase(wordarray[i]);
				System.out.print(wordarray[i]);
			}
		}
		else if(word==word.toUpperCase()){
			System.out.print(word.toLowerCase());
		}
		else{
			System.out.print(word);
		}

	}
}
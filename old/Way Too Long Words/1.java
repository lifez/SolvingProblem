import java.util.Scanner;
public class waytolongword {
	public static void main(String[] arg){
		Scanner in = new Scanner(System.in);
		int limit;
		String word;

		limit = in.nextInt();
		while (limit>0){
			word =in.next();
			char[] words = new char[100];
			words = word.toCharArray();
			if (word.length()>10){
				System.out.format("%s%d%s\n",words[0],word.length()-2,words[word.length()-1]);
			}
			else{
				System.out.format("%s\n",word);
			}
			limit--;
		}
	}
}
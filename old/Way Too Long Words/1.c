#include <stdio.h>
#include <string.h>
int main(){
	int limit;
	char word[50];
	scanf("%d",&limit);
	while (limit>0){
		scanf("%s",&word);
		if(strlen(word)>10){
		printf("%c%d%c\n",word[0],strlen(word)-2,word[strlen(word)-1]);
		limit--;
		}
		else{
			printf ("%s\n",word);
			limit--;
		}
}
}
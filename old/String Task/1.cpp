#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(){
	char x[100];
	int i;
	scanf("%s",&x);
	for (i=0;i<strlen(x);i++){
		if (tolower(x[i])== 'a' || tolower(x[i])== 'e'||tolower(x[i])== 'i'||tolower(x[i])== 'o'||tolower(x[i])== 'u'||tolower(x[i])== 'y'){
			printf("");
		}
		else{
			printf(".");
			printf("%c",tolower(x[i]));
		}
		
	}
	return 0;
	
	
}
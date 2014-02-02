#include <stdio.h>
#include <string.h>
int main(){
	char x[100],n[100];
	int i=0;
	strcpy(n,"NO");
	scanf("%s",&x);	
	for(i;i<strlen(x);i++){
		if (x[i]=='H' || x[i]=='Q' || x[i]=='9'){
			strcpy(n,"YES");
		}
	}
	printf("%s",n);
	return 0;
}

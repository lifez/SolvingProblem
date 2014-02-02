#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <malloc.h>
int main(){
	char x[100],y[100];
	scanf("%s",&x);
	scanf("%s",&y);
	if (strupr(x)>strupr(y)){
		printf("1");
	}
	else if (strupr(x)==strupr(y)){
		printf("0");
	}
	else{
		printf("-1");
	}
	return 0;
	
}
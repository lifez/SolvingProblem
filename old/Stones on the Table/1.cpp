#include <stdio.h>
#include <string.h>
bool all_equal(char array[50]){
	int i=0,count=0;
	
	for(i;i<strlen(array);i++){
		if(array[i]==array[i+1]){
			count++;
		}
	}
	return count==strlen(array)-1; 
	
}
int main(){
	char instone[50];
	int x,i=0,count=0;
	scanf("%d",&x);
	scanf("%s",&instone);
	while (i<x){
		if(instone[i]==instone[i+1]) count++;
		i++;
	}
	if (all_equal(instone)) count = strlen(instone)-1;
	printf("%d",count);
	return 0;
}
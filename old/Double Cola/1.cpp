#include <stdio.h>
int main(){
	int x,y=5;
	char Name[5][20]={
		"Sheldon",
		"Leonard",
		"Penny",
		"Rajesh",
		"Howard"
	};
	scanf("%d",&x);
	while(true){
		if(x<=y){
			y/=5;
			printf("%s",Name[(x-1)/y]);
			break;
		}
		else{
			x-=y;
			y*=2;
		}
	}
	return 0;
}


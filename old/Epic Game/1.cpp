#include <stdio.h>
int gcd(int a,int b){
	int c;
	while(a!=0){
		c=a;
		a=b%a;
		b=c;
	}
	return b;
}
int main(){
	int x,y,z,point=0;
	scanf("%d%d%d",&x,&y,&z);
	while(true){
		if (point==0){
			z-=gcd(x,z);
			if (z<=0){
				printf("0");
				break;
			}
			point++;
		}
		else{
			z-=gcd(y,z);
			if(z<=0){
				printf("1");
				break;
			}
			point--;
		}	
	}
}

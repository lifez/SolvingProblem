#include <stdio.h>
int main(){
	int x,cap=0,maxcap=0,passen[2];
	scanf("%d",&x);
	while (x>0){
		scanf("%d%d",&passen[0],&passen[1]);
		cap-=passen[0];
		cap+=passen[1];
		if (cap>maxcap){
			maxcap=cap;
		}
		x--;
	}
	printf("%d",maxcap);
}

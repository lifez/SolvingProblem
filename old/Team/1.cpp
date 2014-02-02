#include <stdio.h>
int chk(int ans[100],int k){
	int i,n=0;
	for(i=0;i<3;i++){
		if (ans[i]==1)
			n++;
		}
		return n;
	}
int main(){
	int n,problem=0,i,ans[100];
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%d%d%d",&ans[0],&ans[1],&ans[2]);
		if(chk(ans,n)>1){
			problem++;
		}
	}
	printf("%d",problem);
}
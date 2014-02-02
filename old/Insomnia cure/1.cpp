#include <stdio.h>
int chk_hit(int dod, int d, int dragon[]){
	int hit=0;
	while (d!=0){
		if (d%dod==0 && dragon[d-1]==1){
			hit++;
			dragon[d-1]=0;
		}
		d--;
	}
	return hit;
}
int main(){
	int k,l,m,n,d,dragon[100000];
	int i,hit=0;
	scanf("%d",&k);
	scanf("%d",&l);
	scanf("%d",&m);
	scanf("%d",&n);
	scanf("%d",&d);
	for(i=0;i<d;i++){
		dragon[i]=1;
	}
	hit+=chk_hit(k,d,dragon);
	hit+=chk_hit(l,d,dragon);
	hit+=chk_hit(m,d,dragon);
	hit+=chk_hit(n,d,dragon);
	printf("%d",hit);
}

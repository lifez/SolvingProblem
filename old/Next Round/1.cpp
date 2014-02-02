#include <stdio.h>
int main(){
    int limit,Smax,score[100],sum,i,j;
	sum = 0;
	scanf ("%d",&limit);
	scanf("%d",&Smax);
	i =0;
	while (limit>0){
		scanf("%d",&score[i]);
		limit--;
		i++;
	}
	for (j=0;j<i;j++){
		if(score[j]>0 && score[j]>=score[Smax-1]){
			sum++;
		}
	}
	printf("%d",sum);
			
}

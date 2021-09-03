#include<stdio.h>
int main(){
    int *x,y=10,z;
    x=&y;
    scanf("%d",&z);
    printf("%d\n",z);
    printf("Address of y=%d\n",&y);
    printf("Address of x=%d",x);
    return 0;
}

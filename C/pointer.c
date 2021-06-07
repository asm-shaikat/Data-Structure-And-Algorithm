#include<stdio.h>
int main(){
    int *x,y=10;
    x=&y;
    printf("Address of y=%d\n",&y);
    printf("Address of x=%d",x);
    return 0;
}
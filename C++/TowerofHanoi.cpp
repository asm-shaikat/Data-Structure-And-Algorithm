#include<stdio.h>
int main(){
    int q=3;
    data(q,'A','B','C');
}
void data(int n,char x,char y,char z){
    if(n>0){
    data(n-1,x,z,y);
    printf("\n move %c to %c \n",x,y);
    data(n-1,z,y,x);
    }
}

#include<iostream>
#include "linearHeader.h"
#define size 5
using namespace std;
int main(){
  int arr[size]={2,10,12,100,1},n;
  cout<<"Searching for"<<endl;
  cin>>n;
  linearSearch(arr,size,n);
}

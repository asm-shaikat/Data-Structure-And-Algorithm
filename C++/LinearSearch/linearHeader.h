#include<iostream>
using namespace std;
void linearSearch(int arr[],int size,int n){
  int i;
  for(i=0;i<size;i++){
      if(n==arr[i]){
        cout<<n<<" found at index: "<<i<<endl;
      }
  }
}

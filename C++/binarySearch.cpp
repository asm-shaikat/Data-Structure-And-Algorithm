#include<iostream>
using namespace std;
int main(){
  int n;
  cout<<"Enter size of array"<<endl;
  cin>>n;
  int a[n],i,search4,mid,low=0,high;
  cout<<"Enter a sorted array"<<endl;
  for(i=0;i<n;i++){
    cin>>a[i];
  }
  cout<<"Searching for"<<endl;
  cin>>search4;

  while (low<=n) {
    mid=(low+n)/2;
    if(search4==a[mid]){
      cout<<"Element found at index:"<<mid;
      return 0;
    }
    else if(search4>a[mid]){
      low=mid+1;
    }
      else if(search4<a[mid]){
        n=mid-1;
    }
  }
}

#include<iostream>
using namespace std;

bubbleSort(int Q[],int n){
  int i,j,temp;
  for(i=0;i<n;i++){
    for(j=0;j<n-i;j++){
      if(Q[j]>Q[j+1]){
        temp=Q[j];
        Q[j]=Q[j+1];
        Q[j+1]=temp;
      }
    }
  }
  cout<<"After sorting\n";
  for(i=0;i<n;i++){
    cout<<Q[i]<<" ";
  }
}

int main(){
  int n;
  cout<<"Enter size of array"<<endl;
  cin>>n;
  int Q[n],i;
  cout<<"Enter array element\n";
  for(i=0;i<n;i++){
    cin>>Q[i];
  }
  bubbleSort(Q,n);
}

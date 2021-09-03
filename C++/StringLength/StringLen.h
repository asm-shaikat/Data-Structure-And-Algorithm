#include<iostream>
using namespace std;
void strlen(string name){
  int i=0,x=0;
  // for(i=0;name[i]!=NULL;i++){
  //   x++;
  // }
  while (name[i]!=NULL) {
    i++;
    x++;
  }

  cout<<"Length: "<<x<<endl;
}

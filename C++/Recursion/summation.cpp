#include<iostream>
using namespace std;
void sum(int endpoint,int cal,int a){
    if(endpoint==0){
        cout<<"Summation of first "<<a<<" number:"<<cal;
    }else{
        cal = cal + endpoint;
        sum(endpoint-1,cal,a);
    }
}

int main(){
    int endpoints,cal=0,a;
    cout<<"Enter endpoint:";
    cin>>endpoints;
    a = endpoints;
    sum(endpoints,cal,a);
}
#include<bits/stdc++.h>
using namespace std;

unsigned int Hash(int ary [],int numbers ,unsigned int & table_size,int store[]){
    
    for(int i=0;i<numbers;i++){
        int mod = ary[i] % table_size;
        store[mod] = ary[i];
    }

    for(int i=0;i<numbers;i++){
        cout<<" "<<store[i]<<" ";
    }
}

int main(){
    int numbers;
    cout<<"How many number to store? ";
    cin>>numbers;
    int ary[numbers];
    cout<<"Enter number to store:";
    for(int i=0;i<numbers;i++){
        int n;
        cin>>n;
        ary[i] = n;
    }
    unsigned int table_size;
    cout<<"Enter table size: ";
    cin>>table_size;
    int store[table_size];
    Hash(ary,numbers,table_size,store);
}
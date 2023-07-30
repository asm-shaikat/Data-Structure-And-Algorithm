#include<bits/stdc++.h>
using namespace std;

void insert(vector<int> &v){
    int j;
    for(int i = 1; i < v.size();++i){
        int cmp = v[i];
        j = i - 1;
        while(j >= 0 && v[j]>cmp){
            v[j+1] = v[j];
            --j;
    }
    v[j+1] = cmp;
}
 cout<<"Output"<<endl;
    for(auto i : v){
        cout<<i<<" ";
    }
}
int main(){
    vector<int> v;
    int n;
    cin>>n;
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        v.push_back(x);
    }
    insert(v);
}
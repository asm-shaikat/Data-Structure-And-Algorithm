#include<bits/stdc++.h>
using namespace std;

void InsertionSort(vector<int> &v){
    int j;
    for(int i = 1; i < v.size(); ++i){
        int chk = v[i];
        j = i - 1;
        while (j>=0 && v[j]>chk){
            v[j+1] =  v[j];
            j = j-1;
        }
        v[j+1] = chk;

        for (auto i : v)
        {
            cout << i << " ";
        }
        cout << endl;
    }
    // cout<<"After insertion sort"<<endl;
    

}


int main(){
    vector<int> v;
    int n;
    // cout<<"How many digits ? ";
    cin>>n;
    for(int i=0; i<n; i++){
        int x;
        cin>>x;
        v.push_back(x);
    }
    InsertionSort(v);
}
/*
Input:  1234
Output: 10
solve the porblem with log(n) complexity
*/
#include<bits/stdc++.h>
using namespace std;
int digit(int n) {
    if(n==1)
    return 1;
    return (n%10)+digit(n/10);
}
int main(){
    int n;
    cout<<"Enter the digit:";
    cin >> n;
    cout<<"Ans: "<<digit(n);
}
#include <iostream>
//백준 11727문제 2xn 타일링2
using namespace std;
int d[1001];
int dp(int n){
    if(n==1) return 1;
    if(n==2) return 3;
    if(d[n] != 0) return d[n];
    return d[n] = (dp(n-1) + 2*dp(n-2))%10007;
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    cout<<dp(n)<<"\n";
    return 0;
}
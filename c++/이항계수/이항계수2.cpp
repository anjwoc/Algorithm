#include <iostream>

using namespace std;
int d[1001][1001];
int dp(int n, int k){
    if(n==k || k==0) return 1;
    if(d[n][k] != 0) return d[n][k];
    return d[n][k] = (dp(n-1, k) + dp(n-1, k-1))%10007;

}


int main(void){
    int n, k;
    cin>>n>>k;

    cout<<dp(n,k)<<"\n";

    return 0;
}
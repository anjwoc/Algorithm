#include <iostream>

using namespace std;
int dp(int n, int k){
    if(n==k || k==0) return 1;
    return (dp(n-1, k) + dp(n-1, k-1));

}
int main(void){
    int n, k;
    cin>>n>>k;

    cout<<dp(n,k)<<"\n";


    return 0;
}
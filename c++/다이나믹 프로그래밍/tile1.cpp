#include <iostream>
//백준 11726문제 2xn 타일링
using namespace std;
int d[1001];

int dp(int x){
    if (x==1) return 1;
    if (x==2) return 2;
    if(d[x] != 0) return d[x];
    return d[x] = (dp(x-1) + dp(x-2)) % 10007;
}


int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int x;
    cin>>x;
    cout<<dp(x)<<"\n";

    return 0;
}
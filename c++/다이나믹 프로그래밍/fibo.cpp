#include <iostream>

using namespace std;

long long d[100];

long long dp(long long x){
    if (x==1 || x==2) return 1;
    //재귀의 종료 조건
    
    if(d[x] != 0) return d[x];
    return d[x] = dp(x-1) + dp(x-2);
}


int main(void){
    cout<<dp(50)<<endl;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int len(int n){
    int cnt=0;
    while(n--){
        cnt+=1;
        n/=10;
    }
    return cnt;
}

int main(void){
    int s, n;
    cin>>s>>n;
    cout<<s<<n<<endl;

    int r = 2*s+3;
    int c = s+2;
    int length = len(n);
    char arr[r][c*length + length-1]={0,};
    
    cout<<length<<endl;
    

    return 0;
}
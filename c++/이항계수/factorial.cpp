#include <iostream>

using namespace std;
//factorial 0의 개수는 항상 5의 개수가 2의 개수보다 작아서 5의 개수만 구해도 된다.
int zero_len(int n){
    int tmp1=0, tmp2=0;
    int ret=0;
    for(int i=1;i<=n;i++){
        int tmp = i;
        while(!(tmp%5)){
            tmp2+=1;
            tmp/=5;
        }
        while(!(tmp%2)){
            tmp1+=1;
            tmp/=2;
        }
        

    }
    ret = tmp1>tmp2?tmp2:tmp1;
    return ret;
}

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin>>n;

    cout<<zero_len(n)<<"\n";

    return 0;
}
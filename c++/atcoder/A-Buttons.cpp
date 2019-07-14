#include <iostream>
using namespace std;
int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int a,b;
    int ret=0;
    cin>>a>>b;

    //한번누르면 버튼이 1씩 감소 근데 총 두 번 누르는게 가능 
    //거기서 가장 최대의 코인 값을 얻어낼 경우를 구해라
    if(a>b){
        ret += a;
        a-=1;
        if(a>b){
            ret += a;
            a-=1;
        }
        else{
            ret+=b;
            b-=1;
        }
    }
    else{
        ret+=b;
        b-=1;
        if(a>b){
            ret+=a;
            a-=1;
        }
        else{
            ret+=b;
            b-=1;
        }
    }
    cout<<ret;
    return 0;
}
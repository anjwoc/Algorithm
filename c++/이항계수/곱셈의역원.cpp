#include <iostream>
using namespace std;

int main(void){
    int x,a,m;
    cin>>m;

    for(int i=1;i<m;i++){
        if((a*i) % m == 1){
            x=i;
        }
    }

    cout<<x<<endl;
    return 0;
}
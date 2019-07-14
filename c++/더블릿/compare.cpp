#include <iostream>
using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n1, n2;
    cin>>n1>>n2;

    if(n1>n2){
        cout<<">";
    }
    if(n1<n2){
        cout<<"<";
    }
    if(n1==n2) cout<<"=";


    return 0;
}
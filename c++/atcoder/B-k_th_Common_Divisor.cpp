#include <iostream>
#include <vector>
using namespace std;
vector<int> ret(101);
int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int a,b,k;
    cin>>a>>b>>k;
    int result=0;
    
    for(int i=1;i<=a && i<=b;i++){
        if((a%i==0 && b%i==0)){
            ret.push_back(i);
        }
    }
    result = ret[ret.size()-k];
    

    cout<<result;

    return 0;
}
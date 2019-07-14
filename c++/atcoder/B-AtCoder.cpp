#include <iostream>
#include <string>
using namespace std;

int main(void){
    string s;
    int cnt=0;
    int ret=0;
    cin>>s;
    for(int i=0;i<s.size();i++){
        if(s[i] == 'A' || s[i] == 'C' || s[i] == 'G' || s[i] == 'T'){
            cnt++;
            if(ret<cnt) ret = cnt;
        }
        else
            cnt=0;
            
    }
    cout<<ret<<endl;

    return 0;
}
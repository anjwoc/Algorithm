#include <iostream>
using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n1, n2;
    cin>>n1>>n2;
    
    if(n2 == 0){
        cout<<n1<<" | "<<n2<<"\n";
        return 0;
    }

    if(n1>0 && n2<0){
        for(int i=1;i<=(-1*n2);i++){
            if(n2 == n1*i*-1){
                cout<<n1<<" | "<<n2<<"\n";
                return 0;
            }
        
        }
    }
    if(n1>0 && n2>0){
        for(int i=1;i<=n2;i++){
            if(n2 == n1*i){
                cout<<n1<<" | "<<n2<<"\n";
                return 0;
            }
        
        }
    }
    if(n1<0 && n2>0){
        for(int i=-1;i>=(-1*n2);i--){
            if(n2 == n1*i){
                cout<<n1<<" | "<<n2<<"\n";
                return 0;
            }
        
        }
    }
    if(n1<0 && n2<0){
        for(int i=1;i<-1*n2;i++){
            if(n2 == n1*i){
                cout<<n1<<" | "<<n2<<"\n";
                return 0;
            }
        
        }
    }
    
    cout<<n1<<" !| "<<n2<<"\n";


    return 0;
}
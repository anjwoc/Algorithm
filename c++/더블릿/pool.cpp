#include <iostream>
using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin>>n;//지우지 않은 꼭지점의 수
    int xi[n] = {0,};
    int yi[n] = {0,};

    for(int i=0;i<n;i++){
        if(xi[i]<-1000 && xi[i]>1000 && yi[i]<-1000 && yi[i]>1000){
            cout<<"-1";
            exit(0);
        }
        cin>>xi[i]>>yi[i];
    }

    for(int i=0;i<n;i++){
        cout<<"dx: "<<xi[i]<<" dy: "<< yi[i]<<"\n";
        cout<<"i: "<<i<<"\n";
    }

    int dx=0, dy=0;
    dx = yi[1]-yi[0];
    dy = xi[1]-xi[0];
    cout<<dx<<","<<dy<<",";
    if(dx == dy){
        cout<<"-1";
        exit(0);
    }
    cout<<dx*dy;
   

    return 0;
}
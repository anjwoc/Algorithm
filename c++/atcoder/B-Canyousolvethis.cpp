#include <iostream>
using namespace std;

int main(void){
    int n,m,c;
    cin>>n>>m>>c;
    int B[m+1]={0,};
    int A[n+1][m+1]={0,};
    int acc=0, ret=0;
    for(int i=0;i<m;i++){
        cin>>B[i];
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>A[i][j];
        }
    }

    for(int i=0;i<n;i++){
        acc=0;
        for(int j=0;j<m;j++){
            //cout<<"A[i][j]: "<<A[i][j]<<" B: "<<B[j]<<"\n";
            //cout<<"A[i][j]*B[j]: "<<A[i][j]*B[j]<<"\n";
            acc += A[i][j]*B[j];

        }
        //cout<<"acc: "<<acc<<" c:"<<c<<endl;
        if(acc+c > 0)
            ret++;
    }
    cout<<ret<<"\n";

    return 0;
}
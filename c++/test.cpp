#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
int arr[25][25];
int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    string a;
    cin >> a;
    cout<<"Hello World"<<endl;
    cout<<a;
    int tmp;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cin>>tmp;
            arr[i][j] = tmp;
        }
    }

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            cout<<arr[i][j]<<endl;
        }
    }


    return 0;
}
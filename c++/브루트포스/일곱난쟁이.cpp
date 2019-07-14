#include <iostream>

using namespace std;

int main(void){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int arr[9+1] = {0 , };
    int sum=0;
    int ret[7+1] = {0 , };
    for(int i=0;i<9;i++){
        cin>>arr[i];
        sum += arr[i];
    }
    //총합 sum(9개의 합)에서 2개씩 더한 값을 빼서 100인걸 찾는다.
    int cnt=0;
    for(int i=0;i<9;i++){
        for(int j=i+1;j<9;j++){
            int tmp = arr[i] + arr[j];
            if(sum-tmp == 100){
                for(int k=0;k<9;k++){
                    if(k==i || k==j) continue;
                    ret[cnt++] = arr[k];
                }
            }
        }
    }

    for(int i=0;i<7;i++){
        for(int j=i+1;j<7;j++){
            if(ret[j] < ret[i]){
                int tmp=ret[j];
                ret[j]=ret[i];
                ret[i]=tmp;
            }
        }
    }

    for(int i=0;i<7;i++){
        cout<<ret[i]<<" ";
    }

    
    return 0;
}

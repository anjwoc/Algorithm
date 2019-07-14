#include <iostream>

using namespace std;
int length(int N){
    int ret=0;
    while(N){
        ret++;
        N/=10;
    }
    return ret;
}

int main(void){
    int N;
    cin>>N;
    //N은 1000000보다 작거나 같은 자연수
    int len = 0;
    int arr[len+1]={0,};
    int cnt=0;
    // if(N==1023) cout<<"-1"<<"\n";
    // if(N==1022) cout<<"9876543210"<<"\n";
    long long i=1;
    while(i!=0){
        len = length(i);
        if(len==1) cnt+=1;
        else{
            int tmp = i;
            for(int j=len-1;j>=0;j--){
                arr[j] = tmp%10;
                tmp /= 10;
            }
            int cmp = arr[0];
            for(int i=1;i<len;i++){
                if(cmp > arr[i]){
                    if(i == len-1){
                        cnt+=1;
                        break;
                    } 
                    cmp = arr[i];
                }
                else break;
            }
        }
        if(cnt == N){
            cout<<i;
            exit(0);
        }
        i++;
    }
    return 0;
}
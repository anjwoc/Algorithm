#include <iostream>

using namespace std;
/*
각 자릿수가 등차수열을 이루면 '한수'이다.
123, 147, 이런식으로 이루어지면 됌--> 그럼 일의자리, 십의자리는? 모두 한수임
비교할 대상이 없어서 다 한수 취급
110을 예로 들면 1~99까지 전부 한수이고 100~110까지 한수를 이루는 숫자가 없어서 갯수가 99가 출력된다.
*/
int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	int ret = 0;
    if(N<100){
        cout<<N;
        exit(0);
    }
    if(N>=100){
        ret=99;
        for(int i=99;i<=N;i++){
            int tmp = i;
			int n1=tmp/100%10;
            int n2=tmp/10%10;
            int n3=tmp%10;
			if(n2*2 == n1+n3) ret+=1;
        }
    }
    if(N==1000) ret-=1;
	
	cout << ret;

	return 0;
}
#include <iostream>

using namespace std;

int length(int num) {
	int ret = 0;
	while (num) {
		ret++;
		num /= 10;
	}
	return ret;
}

int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	int len = length(N);
	int ret[4] = { 0, };
	int cnt = 0;
	if (N == 0 || N == 1000000) {
		cout << "0";
		exit(0);
	}
	bool check = false;
	int sum = 0;
	for (int i = N-54; i < N; i++) {
		sum = 0;
		int tmp = i;
		cnt = 0;
		for (int j = 0; j < len; j++) {
			ret[j] = tmp % 10;
			cnt+=1;
			sum += ret[j];
			tmp /= 10;
			if (tmp == 0) {
				sum += i;
				break;
			}
		}
		if (sum == N) {
			check = true;
			break;
		}
	}
	if (check == false) {
		cout << "0";
		exit(0);
	}
	for (int i = cnt-1; i >= 0; i--) {
		cout << ret[i];
	}

	return 0;
}
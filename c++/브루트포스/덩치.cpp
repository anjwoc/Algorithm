#include <iostream>

using namespace std;

int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int N;
	cin >> N;
	int ret[3][50 + 1] = { 0, };

	for (int i = 0; i < N; i++) {
		cin >> ret[0][i] >> ret[1][i];
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (i == j)	 continue;
			if (ret[0][i] < ret[0][j] && ret[1][i] < ret[1][j]) {
				ret[2][i] += 1;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		cout << ret[2][i]+1 << "\n";
	}

	return 0;
}
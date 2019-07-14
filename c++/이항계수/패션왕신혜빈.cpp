#include <iostream>
#include <map>
#include <string>
using namespace std;
void check() {
	int n;
	map<string, int> m;
	cin >> n;
	while (n--) {
		auto comp = m.size();
		string type, clothes;
		cin >> clothes >> type;

		m.insert(pair<string, int>(type, 1));

		if (comp == m.size()) {
			m[type]++;
		}
	}

	auto begin = m.begin();
	auto end = m.end();
	auto val = 1;

	for (auto it = begin; it != end; ++it) {
		val *= (it->second + 1);
	}
	cout <<(val - 1) << "\n";
}
int main(void) {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		check();
	}


	return 0;
}
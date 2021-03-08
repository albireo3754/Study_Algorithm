#include <iostream>
#include <string>

using namespace std;

int arr[100001] = {};

int main() 
{
	int n, m;
	int mask;
	for (int i = 0; i < 26; i++) {
		mask |= 1 << i;
	}
	cin >> n >> m;
	string temp;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		for (auto j: temp) {
			arr[i] |= 1 << (j - 'a');
		}
	}

	int o;
	char x;
	for (int i = 0; i < m; i++) {
		cin >> o >> x;
		int count = 0;
		mask ^= 1 << (x - 'a');
		for (int j = 0; j < n; j++) {
			if (arr[j] == (arr[j] & mask)) count++;
		}
		cout << count << endl;
	}

	return 0;
}
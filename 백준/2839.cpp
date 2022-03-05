//2839 설탕배달
// 공부한 내용 : 처음에 바로 5로 나누는 경우와 그렇지 않은 경우로 나누는 부분
#include <iostream>
using namespace std;
int main() {
	int count = 0;
	int n;
	cin >> n;
	
	if (n % 5 == 0) {
		cout << n/5;
		return 0;
	}

	while (n > 0) {
		n = n - 3;
		count++;
		if (n % 5 == 0) {
			count = count + n/5;
			cout << count;
			return 0;
		}
	}
	cout << -1;
	return 0;
}
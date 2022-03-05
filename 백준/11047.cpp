//11047 동전0
// 공부한 내용 : 입력 받은 만큼 배열 할당할 때는 동적으로 할당
#include <iostream>
using namespace std;
int main() {
	int num, price;
	int count = 0;
	cin >> num >> price;
	int* p = new int[num];

	for (int i = 0; i < num; i++) {
		cin >> p[i];
	}

	for (int j = num - 1; j >= 0; j--) {
		count += price / p[j];
		price %= p[j];
	}

	cout << count;
}
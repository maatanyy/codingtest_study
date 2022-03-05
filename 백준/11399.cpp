//11399 ATM
// 공부한 내용 : 버블정렬 
#include <iostream>
using namespace std;
int main() {
	int num;
	int temp;
	int sum = 0;
	cin >> num;
	int* p = new int[num];
	
	for (int i = 0; i < num; i++) {
		cin >> p[i];
	}

	for (int j = 0; j < num - 1; j++) {   //버블정렬 통해 순서 재배열
		for (int k = 0; k < num-1- j; k++) {
			if (p[k] > p[k+1]) {
				temp = p[k];
				p[k] = p[k + 1];
				p[k + 1] = temp;
			}
		}
	}

	for (int t = num; t > 0 ; t--) {
		sum = sum + t * p[num- t];
	}

	cout << sum;

	delete[] p;
	return 0;
}
//2480 주사위 세개
// 공부한 내용 : 어떻게 케이스를 나눠야 하나 고민했다. 특히 모두 다른 경우 어케 나눌지 고민을 했다.
//1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
//같은 눈이 3개가 나오면 10,000원 + (같은 눈)×1,000원의 상금을 받게 된다.
//같은 눈이 2개만 나오는 경우에는 1, 000원 + (같은 눈)×100원의 상금을 받게 된다.
//모두 다른 눈이 나오는 경우에는(그 중 가장 큰 눈)×100원의 상금을 받게 된다.
//예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000 + 3×100으로 계산되어 1,300원을 받게 된다.
//또 3개의 눈이 2, 2, 2로 주어지면 10,000 + 2×1,000 으로 계산되어 12,000원을 받게 된다. 
//3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

#include <iostream>
using namespace std;
int main() {
	int num1, num2, num3;
	cin >> num1 >> num2 >> num3;

	if (num1 == num2 && num2 == num3) {
		cout << 10000 + (num1 * 1000);
		return 0;
	}
	else if(num1 == num2 && num1 != num3) {
		cout << 1000 + (num1 * 100);
		return 0;
	}
	else if (num1 == num3 && num1 != num2) {
		cout << 1000 + (num1 * 100);
		return 0;
	}
	else if (num2 == num3 && num2 != num1) {
		cout << 1000 + (num2 * 100);
		return 0;
	}

	else {
		if (num1 >= num2) {
			if (num1 >= num3) {
				cout << num1 * 100;
				return 0;
			}
			else if (num3 >= num1) {
				cout << num3 * 100;
				return 0;
			}
		}
		else if (num2 >= num1) {
			if (num2 >= num3) {
				cout << num2 * 100;
				return 0;
			}
			else if (num3 >= num2) {
				cout << num3 * 100;
				return 0;
			}
		}		
	}
	
	return 0;
}
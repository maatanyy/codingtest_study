//10162 전자레인지
// 공부한 내용 : a, b, c를 구하는 것 까지는 괜찮았는데 -1이 나오는 예외처리 하는 부분을 고민하다 다른 사람이 푼 방법을 보고 깨달았다
// 만약에 예외의 경우 a,b,c의 값에 올바른 정수값이 안들어가는데 이걸 이용해서 다시 곱해서 원래 수랑 같은 수가 나오는지 비교를 통해 해결했다.
#include <iostream>
using namespace std;
int main() {
	int num;
	int a = 0, b = 0, c = 0;  //a : 300, b : 60, c : 10
	cin >> num;

	a = num / 300;
	b = num % 300 / 60;
	c = num % 300 % 60 / 10;

	if (a * 300 + b * 60 + c * 10 != num) {
		cout << -1;
		return 0;
	}

	cout << a << " "<< b << " "<< c;
	return 0;
}
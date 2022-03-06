//2525 오븐시계
// 공부한 내용 : case를 어떻게 나눌지 생각을 했다. 특히 24시를 넘었을 때 어케 처리할지 고민을 했다.
#include <iostream>
using namespace std;
int main() {
	int si, boon, need;
	int count = 0;
	cin >> si >> boon;
	cin >> need;
	
	if (boon + need < 60) {
		cout << si <<" "<< boon + need;
		return 0;
	}

	else if (boon + need == 60) {
		si += 1;
		boon = 0;
		if (si == 24) {
			si = 0;
			cout << si << " " << boon;
			return 0;
		}
		cout << si << " " << boon;
		return 0;
	}

	else {
		count = (boon + need) / 60;
		boon = (boon + need) % 60;
		
		si += count;
		if (si >= 24) {
			si = si - 24;
			cout << si << " " << boon;
			return 0;
		}
		else {
			cout << si << " " << boon;
			return 0;
		}
	}
	
	return 0;
}
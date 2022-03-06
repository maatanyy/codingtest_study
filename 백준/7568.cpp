//7568 덩치
// 공부한 내용 : 클래스 사용 오랜만에 복습, 등수 메기는 법 어떻게 해야하나 고민
#include <iostream>
using namespace std;

class People {
	int weight, height,up;
public:
	void setPeople(int weight, int height) {
		this->weight = weight;
		this->height = height;
		this->up = 0;
	}

	int getWeight() {
		return weight;
	}

	int getHeight() {
		return height;
	}

	void setUp() {
		up = up + 1;
	}

	int getUp() {
		return up;
	}
};

int main() {
	int peoplenum, weight, height;
	cin >> peoplenum;
	People* point = new People[peoplenum];

	for (int i = 0; i < peoplenum; i++) {
		cin >> weight >> height;
		point[i].setPeople(weight, height);
	}

	for (int t = 0; t < peoplenum; t++) {
		for (int k = 0; k < peoplenum; k++) {   //k=t면 안됨 앞도 다 비교해야 해서 j=0부터 여야함!!
			if ( (point[t].getHeight() < point[k].getHeight()) && (point[t].getWeight() < point[k].getWeight()) ) {  
				point[t].setUp();
			}
		}
	}

	for (int u = 0; u < peoplenum; u++)
		cout << point[u].getUp()+1 << " ";


	delete point;
	return 0;
}
//11651 좌표 정렬하기2
//공부한 내용 : 앞 선 11651번을 풀고 비슷한 11651번을 바로 풀어보니 쉽게 풀 수 있었다
//다만 bool compare함수에서 &아마 기억상 래퍼랜스 같은 데 기억이 가물가물해서 책 보고 다시 봐야할 것 같다.
//모르고 쓰는 기분이랄까
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


//좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
bool compare(const pair<int, int>& p1, const pair<int, int>& p2) {
    if (p1.second == p2.second)
        return p1.first < p2.first;
    return p1.second < p2.second;
}

int main() {
    int n, x, y;
    cin >> n;

    vector<pair<int, int>> v;
    v.assign(n, { 0, 0 });   //백터 입력받은 n개만큼 {0,0}으로 집어 넣는다.

    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        v[i] = { x, y };
    }

    sort(v.begin(), v.end(), compare); 

    for (int i = 0; i < n; i++)
        cout << v[i].first << ' ' << v[i].second << '\n';

    return 0;
}

//[출처] [백준 / C++] 11650번 | 작성자 Kimyu
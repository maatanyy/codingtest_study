//11650 좌표 정렬하기
//공부한 내용 : 벡터의 assign 기능 그리고 sort하는 부분 
//sort 하는 부분을 고민하다 다른 블로그의 글을 참고했는데 매우 인상 깊었다
//나는 x부터 비교하고 그다음에 다시 y비교하는줄 알았는데 바로 x가 같을경우 y하고 아닐경우 x작은거 부터 하는게 인상 깊었다
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const pair<int, int>& p1, const pair<int, int>& p2) {
    if (p1.first == p2.first) return p1.second < p2.second;
    return p1.first < p2.first;
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

    sort(v.begin(), v.end(), compare); // v.beign() ~ v.end() compare통해 정렬

    for (int i = 0; i < n; i++)
        cout << v[i].first << ' ' << v[i].second << '\n';

    return 0;
}

//[출처] [백준 / C++] 11650번 | 작성자 Kimyu
//[참고] https://blog.naver.com/serena35/222646484736
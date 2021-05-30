//입력
//5
//12341234
//11111222
//12122222
//22222222
//12673939
//
//출력
//4
//2
//5
//2
//14
//
//모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
//숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
//두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
//숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
//그 외의 경우 난이도: 10


// 코드 출처 https://dontdiethere.tistory.com/92

#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>

#define endl '\n'
#define fastio cin.sync_with_stdio(false); cin.tie(nullptr)

using namespace std;

const int INF = 987654321;
string N;
int memo[10002];

//N[a..b] 구간의 난이도를 반환
int classify(int a, int b){
    string M = N.substr(a, b-a+1);

    // 모든 문자열이 같은 경우
    if(M == string(M.size(), M[0]))
        return 1;

     // 등차수열 확인
     bool progressive = true;
     for(int i=0;i<M.size()-1;i++) //마지막 전까지 확인
        if(M[i+1] - M[i] != M[1] - M[0])
          progressive = false;

     // 단조 증가, 감소
     if(progressive && abs(M[1] - M[0]) == 1)
        return 2;

     // 두 수가 번갈아 나오는 경우
     bool alternating = true;
     for(int i=0;i<M.size();i++)
        if(M[i] != M[i%2])
            alternating = false;

     if(alternating)
        return 4;

     //공차가 1이 아닌 등차수열인 경우
     if(progressive)
        return 5;

    //나머지
    return 10;

    }


int dp(int begin){
    if(begin == N.size()) //인덱스가 끝에 도달하면
        return 0;

    int &ret = memo[begin];
    if (ret != -1)
        return ret; // 이미 방문했으면 memo 참조값 return

    ret = INF; //큰값 초기화

    // 3~5씩 띄어쓰기 가능
    // 난이도 구하기
    for(int L=3;L<=5;L++)
        if (begin+L <= N.size())
            ret = min(ret, dp(begin + L) + classify(begin, begin + L - 1));
     return ret;

}

int main(){
    fastio;

    int _;
    cin >> _;
    while(_--){
        memset(memo, -1, sizeof(memo)); //메모리 셋팅
        cin >> N;
        cout << dp(0) << endl;
    }

    return 0;
}}
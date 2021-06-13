// 입력
// 3
// 5
// -1000 -1000 -3 -1000 -1000
// 6
// 100 -1000 -1000 100 -1000 -1000
// 10
// 7 -5 8 5 1 -4 -8 6 7 9

// 출력
// -1000
// 1100
// 7

// 테스크 케이스1
// 현) 끝 2개 지우기 LEFT -3 -1000 -1000-1000
// 서) 왼쪽 끝에 2개 3 -1000 지우기   LEFT -1000
// 현) 2개 이하로 남아서 -1000을 가질 수 밖에 없다 

// 현 : -1000, 서: 0
// -1000

// 테스크 케이스2
// 현) 맨 왼쪽 100 선택
// 서) 맨 왼쪽 두개 지우기 LEFT  100 -1000 -1000
// 현) 맨 왼쪽 두개 지우기 LEFT  -1000
// 서) -1000을 가질 수 밖에 없다  

// 현 : 100, 서 : -1000
// 1100


// https://sangdo913.tistory.com/90님 풀이 

#include<cstdio>
#include<cstring>
#define INF 987654321
 
enum TURN {H = 0, S = 1};
int cache[50][50][2], prices[50];
int max(int i1, int i2) {
    return i1 > i2 ? i1 : i2;
}
 
int min(int i1, int i2) {
    return i1 < i2 ? i1 : i2;
}
 
int same(int i1) {
    return i1;
}

// 마이너스로 바꿔주는
int mi(int i1) {
    return -i1;
}
 
int(*cal[2])(int, int) = { max, min };
int(*conv[2])(int i1) = { same, mi };
int rets[2] = { -INF, INF };
 
int diff(int turn, int l, int r) {
    if (l > r) {
        return 0;
    }
 
    int &ret = cache[l][r][turn];
    if (ret != -1) return ret;
 
    ret = rets[turn];
 
    //cal[] : 서하의 경우엔 - 점수가 큰 점수, 따라서 min을 이용해 계산
    //          현우의 경우엔 + 점수가 큰 점수, 따라서 max를 이용해 계산
    //conv[] : 서하의 경우엔 점수를 얻으면 - 실행
    //           현우의 경우엔 점수를 얻으면 + 실행
    ret = cal[turn](ret, diff(turn ^ 1, l + 1, r) + conv[turn](prices[l])); // 왼쪽꺼 하나 떼기
    ret = cal[turn](ret, diff(turn ^ 1, l, r - 1) + conv[turn](prices[r])); //오른쪽꺼 하나 빼기
    if (r != l) {
        ret = cal[turn](ret, diff(turn ^ 1, l + 2, r)); //왼쪽꺼 두개 떼기;
        ret = cal[turn](ret, diff(turn ^ 1, l, r - 2)); // 오른쪽꺼 두개 빼기
    }
 
    return ret;
}
 
int main(){
    int t;
    scanf("%d\n", &t);
 
    while (t--) {
        memset(cache, -1, sizeof(cache));
 
        int n;
        scanf("%d\n", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d \n", &prices[i]);
        }
 
        int res = diff(H, 0, n - 1);
        printf("%d\n", res);
    }
 
    return 0;
}


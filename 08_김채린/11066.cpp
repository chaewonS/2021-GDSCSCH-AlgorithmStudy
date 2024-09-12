#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define INF 1000000

int T, K;
int file[501];
int sum[501];
int dp[501][501];

int main() {
	cin >> T;
	while (T--) { //N번 만큼 반복 (T=테스트 데이터의 개수)
		cin >> K; //K=소설을 구성하는 장의 개수
		for (int i = 1; i <= K; i++) {
			cin >> file[i]; //파일의 크기
			sum[i] = sum[i - 1] + file[i]; //i번째 파일까지의 크기 합 
		}
		for (int i = 1; i <= K; i++) { //i는 구해야 하는 범위의 크기
			for (int j = 1; j <= K - i; j++) { //j는 구해야 하는 범위의 시작 부분
				dp[j][i + j] = INF;
				for (int n = j; n < i + n; n++) //n은 구해야 하는 범위를 두 부분으로 나누는 기준->n이 움직이면서 최소비용을 찾음
					//파일들을 합치는데 필요한 최소비용
					dp[j][i + j] = min(dp[j][i + j], dp[j][n] + dp[n + 1][i + j] + sum[i + j] - sum[j - 1]);
			}
		}
		cout << dp[1][K] << endl;
	}
}
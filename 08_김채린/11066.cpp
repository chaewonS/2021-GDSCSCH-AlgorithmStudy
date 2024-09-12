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
	while (T--) { //N�� ��ŭ �ݺ� (T=�׽�Ʈ �������� ����)
		cin >> K; //K=�Ҽ��� �����ϴ� ���� ����
		for (int i = 1; i <= K; i++) {
			cin >> file[i]; //������ ũ��
			sum[i] = sum[i - 1] + file[i]; //i��° ���ϱ����� ũ�� �� 
		}
		for (int i = 1; i <= K; i++) { //i�� ���ؾ� �ϴ� ������ ũ��
			for (int j = 1; j <= K - i; j++) { //j�� ���ؾ� �ϴ� ������ ���� �κ�
				dp[j][i + j] = INF;
				for (int n = j; n < i + n; n++) //n�� ���ؾ� �ϴ� ������ �� �κ����� ������ ����->n�� �����̸鼭 �ּҺ���� ã��
					//���ϵ��� ��ġ�µ� �ʿ��� �ּҺ��
					dp[j][i + j] = min(dp[j][i + j], dp[j][n] + dp[n + 1][i + j] + sum[i + j] - sum[j - 1]);
			}
		}
		cout << dp[1][K] << endl;
	}
}
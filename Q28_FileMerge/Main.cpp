#include <iostream>
#include <algorithm>
using namespace std;

int testcase;
int fileSize[501];
int sum[501];
int dp[501][501];
const int intmax = 2100000000;

void initData() {
    for (int i = 0; i < 501; i++) {
        fileSize[i] = 0;
        sum[i] = 0;
        for (int j = 0; j < 501; j++) {
            dp[i][j] = 0;
        }
    }
    return;
}

int solve(int i, int j) {
    if (i == j) return 0;
    int minResult = intmax;
    for (int k = 0; k < abs(i - j); k++) {
        minResult = min(minResult, dp[i][i + k] + dp[i + k + 1][j] + sum[j] - sum[i - 1]);
    }
    return minResult;
}

int main() {
    cin >> testcase;
    while (testcase > 0) {
        testcase--;
        initData();
        int fileNum;
        cin >> fileNum;

        for (int i = 1; i <= fileNum; i++) {
            cin >> fileSize[i];
            sum[i] = sum[i - 1] + fileSize[i];
        }

        for (int i = 0; i <= fileNum; i++) {
            for (int j = 1; i + j <= fileNum; j++) {
                dp[j][i + j] = solve(j, i + j);
            }
        }
        cout << dp[1][fileNum] << endl;
    }
    return 0;
}

//This is rediska0123's code
//Download from https://codingcompetitions.withgoogle.com/codejamio/submissions/000000000019ff03/cmVkaXNrYTAxMjM

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <vector>

using namespace std;

const int MAXN = 300;
const int INF = 1e9;

int dp[2][2][2][2][MAXN];

int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	
	ios_base::sync_with_stdio(false);
	
	int t; cin >> t;
	for (int kek = 0; kek < t; kek++) {
		string s; cin >> s;
		for (int i = 0; i < (int)s.length(); i++)
			for (int k1 = 0; k1 < 2; k1++)
				for (int k2 = 0; k2 < 2; k2++)
					for (int k3 = 0; k3 < 2; k3++)
						for (int k4 = 0; k4 < 2; k4++)
							dp[k1][k2][k3][k4][i] = -INF;
		dp[0][0][0][0][0] = 0;
		for (int i = 0; i < (int)s.length(); i++)
			for (int k1 = 0; k1 < 2; k1++)
				for (int k2 = 0; k2 < 2; k2++)
					for (int k3 = 0; k3 < 2; k3++)
						for (int k4 = 0; k4 < 2; k4++) {
							if (s[i] == 'I') {
								int res = -INF;
								if (k1 > 0)
									res = max(res, dp[k1 - 1][k2][k3][k4][i]);
								if (k2 > 0)
									res = max(res, dp[k1][k2 - 1][k3][k4][i]);
								dp[k1][k2][k3][k4][i + 1] = res;
							}
							if (s[i] == 'i') {
								int res = -INF;
								if (k3 > 0)
									res = max(res, dp[k1][k2][k3 - 1][k4][i]);
								if (k4 > 0)
									res = max(res, dp[k1][k2][k3][k4 - 1][i]);
								dp[k1][k2][k3][k4][i + 1] = res;
							}
							if (s[i] == 'O') {
								int res = -INF;
								if (k1 == 0)
									res = max(res, dp[k1 + 1][k2][k3][k4][i] + 1);
								if (k3 == 0)
									res = max(res, dp[k1][k2][k3 + 1][k4][i]);
								dp[k1][k2][k3][k4][i + 1] = res;
							}
							if (s[i] == 'o') {
								int res = -INF;
								if (k2 == 0)
									res = max(res, dp[k1][k2 + 1][k3][k4][i]);
								if (k4 == 0)
									res = max(res, dp[k1][k2][k3][k4 + 1][i]);
								dp[k1][k2][k3][k4][i + 1] = res;
							}
						}
		
		cout << "Case #" << kek + 1 << ": " << dp[0][0][0][0][(int)s.length()] << endl;
	}
	
	return 0;
}


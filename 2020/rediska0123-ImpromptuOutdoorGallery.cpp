//This is rediska0123's code
//Download from https://codingcompetitions.withgoogle.com/codejamio/submissions/000000000019ff03/cmVkaXNrYTAxMjM

#pragma GCC optimize("Ofast,no-stack-protector")
#pragma GCC optimize("unroll-loops")

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <vector>

using namespace std;

const int MAXN = 1300;
const long long INF = 8e18 + 1000;

int x[MAXN], y[MAXN];

int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	
	ios_base::sync_with_stdio(false);
	
	int t; cin >> t;
	for (int kek = 0; kek < t; kek++) {
		int n; cin >> n;
		for (int i = 0; i < n; i++)
			cin >> x[i] >> y[i];
		
		long long ans = INF;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++) {
				long long k1 = (x[i] - x[j]), k2 = (y[i] - y[j]);
				long long res = k1 * y[j] - k2 * x[j];
				long long max_res = -INF, min_res = INF;
				for (int k = 0; k < i; k++) {
					long long cur = k2 * x[k] - k1 * y[k] + res;
					if (cur > 0) {
						if (min_res > cur)
							min_res = cur;
					} else {
						if (max_res < cur)
							max_res = cur;
					}
				}
				for (int k = i + 1; k < j; k++) {
					long long cur = k2 * x[k] - k1 * y[k] + res;
					if (cur > 0) {
						if (min_res > cur)
							min_res = cur;
					} else {
						if (max_res < cur)
							max_res = cur;
					}
				}
				for (int k = j + 1; k < n; k++) {
					long long cur = k2 * x[k] - k1 * y[k] + res;
					if (cur > 0) {
						if (min_res > cur)
							min_res = cur;
					} else {
						if (max_res < cur)
							max_res = cur;
					}
				}
				long long res1 = -max_res, res2 = min_res;
				if (res1 != INF && res2 != INF)
					ans = min(ans, res1 + res2);
			}
		cout << "Case #" << kek + 1 << ": " << ans << endl;
	}
	
	return 0;
}

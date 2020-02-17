//This is rediska0123's code
//Download from https://codingcompetitions.withgoogle.com/codejamio/submissions/000000000019ff03/cmVkaXNrYTAxMjM

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <vector>

using namespace std;

const int MAXN = 3000;

vector <int> gr[MAXN];

bool was[MAXN];
char ans[MAXN];

bool dfs(int v) {
	if (was[v])
		return true;
	was[v] = true;
	for (int to : gr[v]) {
		if (was[to] && ans[to] == ans[v])
			return false;
		ans[to] = 'R' + 'L' - ans[v];
		if (!dfs(to))
			return false;
	}
	return true;
}

int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	
	ios_base::sync_with_stdio(false);
	
	int t; cin >> t;
	for (int kek = 0; kek < t; kek++) {
		int n; cin >> n;
		vector <int> a(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];
		for (int i = 0; i < n; i++)
			gr[i].clear();
		for (int i = 0; i + 1 < n; i += 2) {
			gr[i].push_back(i + 1);
			gr[i + 1].push_back(i);
			gr[a[i] - 1].push_back(a[i + 1] - 1);
			gr[a[i + 1] - 1].push_back(a[i] - 1);
		}
		
		for (int i = 0; i < n; i++)
			was[i] = false;
		for (int i = 0; i < n; i++) {
			if (!was[i]) {
				ans[i] = 'L';
				assert(dfs(i));
			}
		}
		
		cout << "Case #" << kek + 1 << ": ";
		for (int i = 0; i < n; i++)
			cout << ans[i];
		cout << endl;
	}
	
	return 0;
}


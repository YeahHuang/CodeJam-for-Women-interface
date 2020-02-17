//This is rediska0123's code
//Download from https://codingcompetitions.withgoogle.com/codejamio/submissions/000000000019ff03/cmVkaXNrYTAxMjM

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <vector>

using namespace std;

int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	
	ios_base::sync_with_stdio(false);
	
	int t; cin >> t;
	for (int kek = 0; kek < t; kek++) {
		string s; cin >> s;
		int a = 0, b = 0, res = 0;
		for (int i = 0; i < (int)s.length(); i++) {
			if (s[i] == 'I') {
				a++;
			} else if (s[i] == 'O') {
				if (a > 0)
					a--, res++;
				else
					b--;
			} else if (s[i] == 'i')
				b++;
			else if (s[i] == 'o') {
				if (b == 0) {
					a--;
					b++;
				}
				b--;
			}
			assert(b >= 0);
		}
		assert(a == 0 && b == 0);
		cout << "Case #" << kek + 1 << ": " << res << endl;
	}
	
	return 0;
}

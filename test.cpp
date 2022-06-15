#include <bits/stdc++.h>

using namespace std;

char s[100], buf[100];

int main() {
	
	while(scanf("%s",s) == 1) {
		
		if (strlen(s) != 15) {
			
			puts("incorrect input value");
			continue;
		}
		
		int res = 0;
		for (int i = 0; i < 13; i += 2) {
			res += s[i] + s[i+1] - '0' - '0';
			cout<<(s[i]-'0' + s[i+1] - '0') % 10;
		}
		
		cout<<s[0]<<endl;
		
	}
	
	
	
	return 0;
}
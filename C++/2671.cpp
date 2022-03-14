#include <iostream>

using namespace std;

bool submarine(string n){
	int i=0;
	int s=n.size();

	while (i<s){
		if (n[i]=='1'){
			if (i+3>=s) return false;
			if (!(n[i+1]=='0' && n[i+2]=='0')) return false;
			i+=1;
			while (i<s && n[i]=='0'){
				i+=1;
			}
			if (i>=s) return false;
			i+=1;
			while (i<s && n[i]=='1'){
				if (i+2<=s && n[i+1]=='0' && n[i+2]=='0') break;
				i+=1;
			}
		}
		else{
			if (i+1>=s) return false;
			if (n[i+1]!='1') return false;
			i+=2;
		}
	}
	return true;
}

int main(void){
	string n;
	cin >> n;

	if (submarine(n)){
		cout << "SUBMARINE";
	}
	else{
		cout << "NOISE";
	}
}
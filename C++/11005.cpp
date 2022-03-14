#include <iostream>
#include <vector>

using namespace std;

int main(void){
	vector<int> v;

	int n;
	cin >> n;

	int b;
	cin >> b;

	while (n>=b){
		v.push_back(n%b);
		n=n/b;
	}

	v.push_back(n);

	for (int i=v.size()-1; i>=0; i--){
		if (v[i]>=10){
			cout << char('A'+(v[i]-10));
		}
		else{
			cout << v[i];
		}
	}
}
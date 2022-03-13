#include <iostream>
#include <vector>

using namespace std;

int main(void){
	int answer=0;

	int n;
	cin >> n;
	int sum;
	cin >> sum;

	vector<int> v(n); // (n) 안 해서 잠깐 헤맸었음 
	for (int i=0; i<n; i++){
		cin >> v[i];
	}

	for (int i=0; i<v.size(); i++){
		int tmp=0;
		for (int j=i; j<v.size(); j++){
			tmp+=v[j];
			if (tmp==sum){
				answer+=1;
				break;
			}
		}
	}
	
	cout << answer;
}
// 1. 파이썬의 if ~ in ~ 를 #include <algorithm>; 
// if (*find(~.begin(), ~.end(), 값)==값) 이용해서 구현 -> 시간 초과

// 2. 이진 탐색 -> 방법은 맞았지만 디테일이 조금 부족해서 시간 초과
// - 이진 탐색은 함수로 따로 빼주기 
// - end=mid-1임
// - ios::sync_with_stdio(0); cin.tie(0);  

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 함수로 따로 빼줄 때 매개변수로 넣어주기 싫으면 전역변수로 
vector<int> number_a; 
int n;

// 이진 탐색 -> 함수로 따로 빼주기 
void binarySearch(int target){
	int start=0;
	int end=n-1;
	int mid;
	while (start<=end){
		mid=(start+end)/2;
		if (target<number_a[mid]){
			end=mid-1; // 나는 여기 end=mid로 했었음   
		}
		else if (target>number_a[mid]){
			start=mid+1;
		}
		else if (target==number_a[mid]){
			cout << 1 << "\n";
			return;
		}
	}
	cout << 0 << "\n"; // 함수로 빼면 return 처리할 수 있기 때문에 0인 상황도 깔끔히 처리 가능 
}

int main(void){
	// 시간 초과 해결 
    ios::sync_with_stdio(0);
    cin.tie(0);  
	
	cin >> n;

	for (int i=0; i<n; i++){
		int x;
		cin >> x;
		number_a.push_back(x);
	}

	sort(number_a.begin(), number_a.end()); //number_a.sort() 아님 

	int m;
	cin >> m;

	for (int i=0; i<m; i++){
		int y;
		cin >> y; // [1,3,7,9,5] 모을 벡터 필요 없음 
		binarySearch(y);
	}

}
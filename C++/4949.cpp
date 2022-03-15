#include <iostream>
#include <stack>

using namespace std;

bool checkBracket(string s){
	stack<char> bracket;
	
	for (int i=0; i<s.size(); i++){
		if (s[i]=='('){
			bracket.push(s[i]);
		}
		else if (s[i]=='['){
			bracket.push(s[i]);
		}
		// else if (s[i]==']' && bracket.empty() && bracket.top()!='[')
		// 이면 bracket.pop(); 하는 코드는
		// ]만 있는 문장을 못 걸러냄 
		else if (s[i]==']'){
			if (bracket.empty() || bracket.top()!='['){
				return false;
			}
			bracket.pop();
		}
		else if (s[i]==')'){
			if (bracket.empty() || bracket.top()!='('){
				return false;
			}
			bracket.pop();
		}
	}
	if (bracket.empty()){
		return true;
	}
	else{
		return false;
	}
}

int main(void){
	ios::sync_with_stdio(false);
	cin.tie(0);

	string s; 

	while (getline(cin, s)){
		if (s=="."){
			break;
		}
		if (checkBracket(s)){
			cout << "yes" << "\n";
		}
		else{
			cout << "no" << "\n";
		}
	}
}
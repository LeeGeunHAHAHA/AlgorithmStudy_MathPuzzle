#include<iostream>

using namespace std;
int n;
int car;
int p, m;
int ans;

int main(){
	cin>>n>>car;
	for(int i =0; i< n; i++){
		cin>>p>>m;
		car = car +p - m;
		if (car < 0) {
			ans =0;
			break;
		}
		ans = (ans > car)? ans:car;
	}
	cout <<ans<<endl;
	return 0;
}

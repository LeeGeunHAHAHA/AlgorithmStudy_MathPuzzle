#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

void getInput(vector<int> &cards){
	int n;
	cin>>n;
	for(int i=0; i<n; i++){
		int card; cin>>card;
		cards.push_back(card);
	}
   
}
int main(){
	int testCase;
	cin>>testCase;

	while(testCase--){
	vector<int> cards;
	getInput(cards);
    
	for(int i=0; i<cards.size(); i++){
		cout<<cards[i]<<" ";;
	}cout<<endl;
	}
	return 0;
}

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int all[9];
vector <int > dwrf;
int main(){
	int tmp, sum;
	sum =0;
	for(int i =0; i<9; i++){
		cin>>tmp;
		all[i]=tmp;
		sum+=tmp;
	}
	for(int i =0; i<9 ; i++ ){
		for(int j =i+1; j<9; j++){
			if(sum -all[i] - all[j]==100){
				for(int a = 0 ; a<9; a++){
					if(a==i||a==j)continue;
					dwrf.push_back(all[a]);
				}
			}
		}
	}
	
	sort(dwrf.begin(),dwrf.end());
	for(int i =0; i<7; i++){
	cout<<dwrf[i]<<endl;
	}
	return 0;
	
}

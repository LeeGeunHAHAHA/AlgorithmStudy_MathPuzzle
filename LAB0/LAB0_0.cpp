#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int* findMinMax(int* tenNums, int a, int b, int c, int d, int e);

int main(){
	fstream in("Lab0-1.dat");
	int* tenNums = new int[10];
	for(int i=0; i<10; i++){
		in>>tenNums[i];
	}
	int* ans= findMinMax(tenNums,0,0,0,tenNums[0],tenNums[0]);

	cout<<"Minium number is "<< ans[2]<<" at position "<<++ans[0]<<endl;
	cout<<"Maximum number is "<< ans[3]<<" at position "<<++ans[1]<<endl;
	return 0;
}
int* findMinMax(int* tenNums,int pos, int minPos, int maxPos, int min, int max){
	int* ans = new int[4];
	if(pos==10){
		ans[0]=minPos;
		ans[1]=maxPos;
		ans[2]=min;
		ans[3]=max;
		return ans;
	}
	int mp = minPos;
	int Mp = maxPos;
	int m = min;
	int M = max;
	if(tenNums[pos] <= m){
		m = tenNums[pos];
		mp = pos;
	}
	if(tenNums[pos] >= M){
		M = tenNums[pos];
		Mp = pos;
	}
	return findMinMax(tenNums, ++pos, mp, Mp, m , M);
				
	
}

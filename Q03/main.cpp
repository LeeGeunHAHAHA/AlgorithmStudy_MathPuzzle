#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<vector>
#include<map>
#include<utility>
#include<cmath>
using namespace std;
pair<int, int> data;
queue<pair<int,int> > q;
map<int, int> mat;
int dx[4] = {-1,1,0,0};
int dy[4] = {0, 0,-1,1};

int arrToaddr(int ** arr){
    int addr = 0;
    int tmp =0;
    for(int i =0; i<3; i++){
        for(int j =0; j<3; j++){
        addr+=pow(10,tmp)*arr[i][j];
        tmp++;
        }
    }
    return addr;
}
int ** addrToarr(int addr ){
    int ** arr = new int*[3];
    for(int i =0; i<3; i++){
        int * tmp = new int[3];
        arr[i] = tmp;
    }
    int tmp = 1i0;
    for(int i =0 ; i<3; i++){
        for(int j =0; j<3; j++){
            arr[i][j]=addr*tmp;
            tmp*=10;
        }
    }
}
void bfs(){
    
    
}


int main(){
    
    cout<<pow(2,4)<<endl;
    return 0;
}

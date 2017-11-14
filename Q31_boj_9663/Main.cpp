#include<iostream>
#include<stdlib.h>
using namespace std;
int ans;
int **map;
int n;
void getInput(){
    cin>>n;
    map = new int*[n];
    for(int i =0; i<n; i++){
        int * tmp = new int[n];
        for(int j =0; j< n ;j++){
            tmp[j]=0;
        }
        map[i] = tmp;
    }
}
void test(){
    for(int i =0; i< n; i++){
        for(int j =0; j< n; j++){
            cout<<map[i][j]<<" ";
         } cout<<endl;
    }
    cout<<endl;
}
bool canPos(int level, int column){
    int c = column;
    int l = level;
    int i =l,j = c;
    
    for(int i =0; i<n ;i++)
        if(map[i][c])
            return false;
    
    while(i>=0 && j>=0){
        if (map[i][j])
            return false;
                i--; j--;
    }
    i = l, j =c;
    while(i>=0 && j<n) {
        if (map[i][j])
            return false;
            i--; j++;
    }
    
    return true;

}
void func (int level){
            test();
    if (level == n) return;
    int l = level;
    for(int i =0; i<n; i++){
        if(canPos(level,i)){ 
            map[l][i] = 1;
            if(level == n-1)ans++;
        }else continue;
        func(l+1);
        map[l][i] = 0;
    }
    return ;
}
int main(){
    getInput();
    func(0);
    cout<<ans<<endl;


    return 0;
}

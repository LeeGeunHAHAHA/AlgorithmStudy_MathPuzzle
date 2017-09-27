#include<iostream>
using namespace std;
int d[12];
int main(){

    d[0]=0;
    d[1]=1;
    d[2]=2;
    d[3]=4;
    int testCase;
    cin>>testCase;
    while(testCase--){
        int n;
        cin>> n;
        for(int i =4; i<12; i++){
            d[i] = d[i-1]+d[i-2]+d[i-3];
        }
        cout<<d[n]<<endl;
        
    }
    return 0;
}

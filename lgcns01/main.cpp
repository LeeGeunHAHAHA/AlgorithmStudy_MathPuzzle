#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int main(){

    int testCase;
    cin>>testCase;
    while(testCase--){
        int numOfPair;
        cin>>numOfPair;
        vector< pair <int, int> > functions;
        while(numOfPair--){
           int a, b;
           cin>>a>>b;
           pair<int , int> tmp(a,b);
           functions.push_back(tmp);
        }  
    
    }
    return 0;
}

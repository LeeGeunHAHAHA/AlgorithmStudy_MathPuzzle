#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
    int testCase;
    cin>>testCase;
    while(testCase--){
        int h, w,n;
        cin>> h>> w>> n;
        int * modh = new int[h+1];
        for(int i=0; i<h; i++)modh[i]=i;modh[0]=h;
        printf("%d%02d\n", modh[n%h],n%h==0?n/h:n/h+1);
        delete modh;
    }
    return 0; 
}

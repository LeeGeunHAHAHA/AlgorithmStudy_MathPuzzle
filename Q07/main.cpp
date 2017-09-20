#include<algorithm>
#include<iostream>
using namespace std;

int d[100001];

int * getData(int n){
    int * data = new int[n];
    for(int i =0; i< n; i++){
    cin>>data[i];
    }
    return data;
}
void dp(int * data, int len){
    d[0] = data[0];
    for(int i =1; i<len; i++){
       if (d[i-1]>=0)d[i] = d[i-1]+data[i];
       else d[i] = data[i];
    }
    sort(d,d+len);
    cout<<d[len-1]<<endl;
}

int main(){
    int n ;
    cin>>n;
    int * data = getData(n);
    dp(data,n);


}

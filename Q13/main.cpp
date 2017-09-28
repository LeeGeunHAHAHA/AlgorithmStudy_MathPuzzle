
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
bool func(int i, int j){
    int a = i; int b = j;
    if(a<0)a*=-1;
    if(b<0)b*=-1;
    return a<b;
}
int main(){
    int testCase;
    cin>>testCase;
    while(testCase--){
        int n, k;
        cin>>n>>k;
        int* arr=new int[n];
        for(int i =0; i<n ; i++){
            int tmp;
            cin>>tmp;
            arr[i]=tmp;
        }
        sort(arr,arr+n);
        int index=0;
        vector<int> sums;
        for(int i =0; i< n; i++){
            int lower = lower_bound(arr+i, arr+n, k-arr[i])-arr;
            if(abs(arr[i]+arr[lower-1]-k)<abs(arr[i]+arr[lower]-k))index =lower-1;
            else index =lower;
            if(i!= index){
                if(sums.size()==0)
                    sums.push_back(arr[i]+arr[index]-k);
                else{
                    if(abs(sums[0]-k)>abs(arr[i]+arr[index]-k))sums[0]=arr[i]+arr[index]-k;
                    else if(abs(sums[0]-k)==abs(arr[i]+arr[index]-k))sums.push_back(arr[i]+arr[index]-k);
                }
            }

        }


        cout<<sums.size()<<endl;
    }
    return 0;
}


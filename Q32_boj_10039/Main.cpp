#include<iostream>
using namespace std;

int main(){
    int sum =0;
    for(int i =0; i<5; i++){
    int tmp;
    cin>>tmp;
    sum += tmp>40? tmp : 40;
    }
    cout<<sum/5<<endl;

    return 0;
}

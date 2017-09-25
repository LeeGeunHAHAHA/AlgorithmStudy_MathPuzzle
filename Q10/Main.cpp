/*
 *solve 10448 eureka by bruteforece
 * */
#include<iostream>
#include<fstream>

using namespace std;

//solve number by brute force!!
bool isEureka(int n){
    int a,b,c;
    for(int i =1; i<=n; i++){
        for(int j=1; j<=n; j++){
            for(int k=1; k<=n; k++){
                a = i*(i+1)/2;
                b = j*(j+1)/2;
                c = k*(k+1)/2;
                if(n==a+b+c) return true;
            }
        }
    }
    return false;

}   

int main(){
    ifstream in; in.open("input.txt");
    int testCase;
    in>>testCase;
    while(testCase--){
        int n; in>>n;
        cout<<isEureka(n)<<endl;
    }
    return 0;
}

#include<iostream>

using namespace std;

int  palin[22];
int makeNum(int b, int input){
   int i =0;
   while(input>0){
    palin[i]=input%b;
    input/=b;
    i++;
   } 
   return i;
}
bool isPalin(int len, int index){
    int oppo = len - index -1; 
    if(index == len/2 ) return true;
    else if(palin[index]==palin[oppo])return isPalin(len,index+1);
    else return false;
}
void calc(int input){
            for(int i =64; i>1; i--){
           int len= makeNum(i, input);
           if(isPalin(len,0)){
               cout<<1<<endl;
               for(int j =0; j< len ; j++){
               cout<<palin[j]<<" ";
               }cout<<'\n'<<i<<endl;
               return;
           }
        }
    
    cout<<0<<endl;
}

int main(){
   int testCase;
   cin>>testCase;
  while(testCase--){
    int input;
    cin>>input;
    calc(input);
  } 
  return 0;
}

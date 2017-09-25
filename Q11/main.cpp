#include<stdio.h>

int g(int a,int b){return b==0 ? a : g(b,a%b);}
int main(){
    int testCase;
    int x;
    scanf("%d" , &testCase);
    int a;
    int b;
    while(testCase--){
        scanf("%d %d", &a,&b);
        while(a!=1){
            b%a==0?x=b/a:x=b/a+1;
            int G = g(a,b);
            a = a*x -b;
            b*=x;
            b/=G;a/=G;
        }
        printf("%d\n", b);

    }
    return 0;
}

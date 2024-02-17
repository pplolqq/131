#include<iostream>
#define N 1000000
using namespace std;
int Next[N];
int main(){
    // int n;
    // cin>>n;
    string s1="aadwadwa";
    // cin>>s1;
    int n=s1.length();
    Next[0]=0;
    int pc=0;
    int res=0;
    for( int idx=1; idx<s1.length();idx++){
        char v= s1[idx];
        while (pc  && s1[pc] != v){
            pc=Next[pc-1];
        }
        if (s1[pc]==v){
            pc++;
        }
        Next[idx]=pc;
        if (idx+1==2*pc){
            res=max(pc,res);
        }
    }
    if (res+Next[n-1]==n){
        cout<<res;
    }
    else{
        cout<<n-Next[n-1];
    }
}
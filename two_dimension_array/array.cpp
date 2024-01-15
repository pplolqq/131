#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int **a=new int * [n];
    int t=1;
    for(int i=0;i<n;i++){
        a[i]=new int [n];
        for(int j=0;j<n;j++){
            a[i][j]=t++;
        }
    }
}
#include<iostream>
using namespace std;
void match(const string & mat,int *comlen){
    int n=mat.length(),pc=0;
    comlen[0]=0;
    for(int i=1;i<n;i++){
        char v=mat[i];
        while (pc && mat[pc]!=v){
            pc=comlen[pc-1];
        }
        if (mat[pc]==v){
            pc++;
        }
        comlen[i]=pc;
    }
}
void kmp(const string & str ,const string & mat){
    int n1=str.length();
    int n2=mat.length();
    int * comlen =new int[n2];
    match(mat,comlen);
    int pc=0,pos=0;
    for(int i=0;i<n1;i++){
        char v=str[i];
        while(pc && mat[pc]!=v){
            pc=mat[pc-1];
        }
        if (mat[pc]==v){
            pc++;
        }
        if (pc==n2){   //pc-i+1 即为匹配位
            pos=pc-i+1;  
            pc=mat[pc-1];
        }
    }
    delete [] comlen;
}
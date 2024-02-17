#include<iostream>
using namespace std;
/*
ABAABABE
ABAB
0012
*/
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
/*
int match(string str,string mat,int *next){
    int p1=0,p2=0;
    int n1=str.length(),n2=mat.length();
    int t=0;
    while(p1<n1){
        if(str[p1]==mat[p2]){
            p1++;
            p2++;
        }
        else{
            if(p2==0){
                p1++;
            }
            else{
                p2=next[p2-1];//保留配对项
            }
        }
        if(p2==n2){ // 匹配成功
            t++;
            p2=next[p2-1]; //保留配对项
        }
    }
    return t;
    // return -1;
void next_array(string str,int *array){
    int n=str.length();
    int pc=0,i=1;
    array[0]=0;
    while (i<=n-1){
        if (str[pc]==str[i])
            array[i++]=++pc;//进1  右移共同长度
        else{
            if(pc!=0)
                pc=array[pc-1]; //找到一个符合的已有值
            else
                array[i++]=0; //没找到，设为0，进1
        }
    }
}
}*/
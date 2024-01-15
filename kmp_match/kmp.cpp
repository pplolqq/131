#include<iostream>
using namespace std;
/*
ABAABABE
ABAB
0012
*/
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
}
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
int main(){
    string s="ABCABDAB";
    string mat="ABCAB";
    int arr[100];
    next_array(mat,arr);
    // for(int i=0;i<mat.length();i++){
    //     cout<<arr[i]<<" ";
    // }
    cout<<match(s,mat,arr);
}
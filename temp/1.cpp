// #include<iostream>
// using namespace std;
// #define N 200
// void match(const string & mat,int *comlen){
//     int n=mat.length(),pc=0;
//     comlen[0]=0;
//     for(int i=1;i<n;i++){
//         char v=mat[i];
//         while (pc && mat[pc]!=v){
//             pc=comlen[pc-1];
//         }
//         if (mat[pc]==v){
//             pc++;
//         }
//         comlen[i]=pc;
//     }
// }
// int kmp(const string & str ,const string & mat,int diff){
//     int n1=str.length();
//     int n2=mat.length();
//     int * comlen =new int[n2];
//     match(mat,comlen);
//     int pc=0,pos=0;
//     for(int i=0;i<n1;i++){
//         char v=str[i];
//         while(pc && mat[pc]!=v){
//             pc=comlen[pc-1];
//         }
//         if (mat[pc]==v){
//             pc++;
//         }
//         if (pc==n2){   //pc-i+1 即为匹配位
//             pos=i;  
//             pc=comlen[pc-1];
//         }
//     }
//     delete [] comlen;
//     return pos;
// }
// int main(){
//     string strlist[N]={"A","B","AB"};
//     int n=3;
//     string str="AAABABABACAV";
//     int  res=0;
//     int n2=str.length();

// }

#include<iostream>
#define N 1000000
using namespace std;
int Next[N];
int main(){
    int n; cin>>n;
    string s1; cin>>s1;
    Next[0]=0; int pc=0;
    for( int idx=1; idx<s1.length();idx++){
        char v= s1[idx];
        while (pc  && s1[pc] != v) pc=Next[pc-1];
        if (s1[pc] == v) pc++;
        Next[idx]=pc;
    }
    cout<<n-Next[n-1];
}
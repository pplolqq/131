#include<stdio.h>
void big(int *a ,int *b){
  int temp;
  if (*a>*b){
    temp=*a;
    *a=*b;
    *b=temp;
  }
}
int main(){
  int a,b;
  a=2;
  b=1;
  // big(&a,&b);
  // scanf("%d ",&a);
  // scanf("%d",&b);
  printf("%lf",2.1/2.1);
}
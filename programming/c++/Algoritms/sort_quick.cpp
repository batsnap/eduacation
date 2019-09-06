#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void qsort(int a[],int b, int e)
{
  int l=b;
  int r=e;
  int k;
  int piv=a[(l+r)/2];
  while (l<=r)
  {
    while(a[l]<piv)
    {
      l++;
    }
    while(a[r]>piv)
    {
      r--;
    }
    if (l<=r)
    {
      k=a[l];
      a[l]=a[r];
      a[r]=k;
      r--;
      l++;
    }
  }
  if (b<r)
  {
    qsort(a,b,r);
  }
  if (e>l)
  {
    qsort(a,l,e);
  }
}

int main(){
  srand(time(NULL));
  int n,s;
  n=-1;
  while (n<=0){
      cin>>n;
  }
  int a[n];
  for(int i=0; i<n; i++){
      a[i]=rand()%100;
      cout<<a[i]<<" ";
  }
  cout<<endl;
  qsort(a,0,n-1);
  for(int i=0; i<n; i++){
  cout<<a[i]<<" ";
  }
  cout<<endl;
  return 0;
}

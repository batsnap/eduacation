#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
void swap(int a, int b)
{
        a=a+b;
        b=a-b;
        a=a-b;
}
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

int main()
{
    srand(time(NULL));
    int n,m;
    cin>>n;
    cin>>m;
    int matrix[n][m];
    int arr[n*m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            matrix[i][j]=rand()%10;
            cout<<matrix[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<endl;
    for(int i=0;i<n*m;i++)
    {
        arr[i]=matrix[i%n][i%m];
    }
    cout<<endl;
    qsort(arr,0,n*m);
    for(int i=0;i<n*m;i++)
    {
        matrix[i/n][i%m]=arr[n*m-i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cout<<matrix[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<endl;
    return 0;
}
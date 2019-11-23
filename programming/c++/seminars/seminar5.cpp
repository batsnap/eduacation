#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int max(int *a,int n)
{
    int s=a[0];
    for(int i=0;i<n;i++)
        if (a[i]>s)
            s=a[i];
    return s;
}

int sum(int *a,int n)
{
    int s=0;
    for(int i=0;i<n;i++)
        s+=a[i];
    return s;
}
int main()
{
    srand(time(0));
    int n; cin>>n;
    int *arr=new int[n];
    for(int i=0;i<n;i++)
        cout<<(arr[i]=5+rand()%16)<<" ";
    cout<<endl<<"max="<<max(arr,n)<<endl<<"sum="<<sum(arr,n)<<endl;
    return 0;
}
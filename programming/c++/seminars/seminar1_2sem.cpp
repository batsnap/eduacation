#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
double sred(int arr[],int n)
{
    double s=0;
    for(int i=0;i<n;i++)
        s+=arr[i];
    return s/n;
}
int main()
{
    srand(time(0));
    int n;
    cin>>n;
    int *arr=new int[n];
    for(int i=0;i<n;i++)
        cout<<(arr[i]=5+rand()%16)<<" ";
    cout<<endl<<sred(arr,n)<<endl;;
    return 0;
}
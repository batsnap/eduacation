#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int SsSsS(char arr[],int n)
{
    int s=0;
    for(int i=0;i<n;i++)
    {
        if (arr[i]=='s' || arr[i]=='S')
            s+=1;
    }
    return s;
}
int main()
{
    int n;
    cin>>n;
    char *arr=new char[n];
    cin>>arr;
    cout<<endl<<SsSsS(arr,n)<<endl;
    return 0;
}
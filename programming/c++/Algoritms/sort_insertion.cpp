#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

void insertion_sort(int a[], int n)
{   
    int j,key;
    for(int i=0;i<n;i++)
    {
        j=i-1;
        key=a[i];
        while ((a[j]>key) && (j>=0))
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=key;
    }
}

int main()
{
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
    insertion_sort(a,n);
    for(int i=0; i<n; i++){
    cout<<a[i]<<" ";
    }
    cout<<endl;
    return 0;
}

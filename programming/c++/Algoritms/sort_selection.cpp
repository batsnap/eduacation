#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

void selection_sort(int a[], int n)
{   
    int k;
    for(int i=0;i<n;i++)
    {
        k=i;
        for(int j=i+1;j<n;j++)
        {
            if (a[j]<a[k])
            {
                k=j;
            }
        }
        swap(a[i],a[k]);
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
    selection_sort(a,n);
    for(int i=0; i<n; i++){
    cout<<a[i]<<" ";
    }
    cout<<endl;
    return 0;
}

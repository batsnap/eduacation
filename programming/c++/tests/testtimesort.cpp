#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;
void bubble_sort(int a[],int n)
{
    int s;
    for(int i=0;i<(n-1);i++){
        for(int j=0;j<(n-1-i);j++){
            if(a[j]>a[j+1]){
                s=a[j];
                a[j]=a[j+1];
                a[j+1]=s;
            }
        }
    }

}

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
    double s1,s2,s3,s4,time1;
    s1=s2=s3=s4=0;
    int n=1000;
    int s=10000;
    int a[n];
    for(int i=0;i<s;i++)
    {
        for(int j=0; j<n; j++)
        {
            a[j]=rand()%1000;
        }
        time1=clock();
        qsort(a,0,n);
        s1+=(clock()-time1)/1000.0;
        time1=clock();
        bubble_sort(a,n);
        s2+=(clock()-time1)/1000.0;
        time1=clock();
        selection_sort(a,n);
        s3+=(clock()-time1)/1000.0;
        time1=clock();
        insertion_sort(a,n);
        s4+=(clock()-time1)/1000.0;
        cout<<i<<endl;
    }
    cout<<"Qsort:"<<s1/float(s)<<endl;
    cout<<"Bsort:"<<s2/float(s)<<endl;
    cout<<"Ssort:"<<s3/float(s)<<endl;
    cout<<"Isort:"<<s4/float(s)<<endl;
    return 0;
}
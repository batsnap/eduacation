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
    int n,s;
    n=-1;
    while (n<=0)
    {
        cin>>n;
    }
    int a[n];
    for(int i=0; i<n; i++) 
    {
        a[i]=rand()%1000;
    }
    double start_time1=clock();
    qsort(a,0,n);
    double end_time1=clock();
    double search_time1=(end_time1-start_time1)/100000.0;
    cout<<"qsort:"<<search_time1<<endl;
    double start_time3=clock();
    insertion_sort(a,n);
    double end_time3=clock();
    double search_time3=(end_time3-start_time3)/100000.0;
    cout<<"insertion_sort:"<<search_time3<<endl;
    double start_time4=clock();
    selection_sort(a,n);
    double end_time4=clock();
    double search_time4=(end_time4-start_time4)/100000.0;
    cout<<"selction_sort:"<<search_time4<<endl;
    double start_time2=clock();
    bubble_sort(a,n);
    double end_time2=clock();
    double search_time2=(end_time2-start_time2)/100000.0;
    cout<<"bubble_sort:"<<search_time2<<endl;
    return 0;
}
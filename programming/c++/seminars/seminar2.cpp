#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <math.h>
using namespace std;
double sum(double a[],int n)
{
    int s=0;
    for(int i=0;i<n;i++)
    {
        s+=a[i];
    }
    return s;
};
void bubble_sort(double a[],int n)
{
    double s;
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
double max(double a[],int k)
{
    double max=a[0];
    for(int i=0;i<k;i++)
    {
        if (max<a[i]){
            max=a[i];
        }
    }
    return max;
}
double min(double a[],int k)
{
    double min=a[0];
    for(int i=0;i<k;i++)
    {
        if (min>a[i]){
            min=a[i];
        }
    }
    return min;
}
int main()
{
    srand(time(NULL));
    double a=-4.2,b=7.3;
    int k;
    cin>>k;
    double arr[k];
    for(int i=0;i<k;i++)
    {
        arr[i]=a+abs(fmod(rand(),b-a+0.1));
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    bubble_sort(arr,k);
    for(int i=0;i<k;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    cout<<sum(arr,k)<<endl;
    cout<<sum(arr,k)/k<<endl;
    cout<<min(arr,k)<<endl;
    cout<<max(arr,k)<<endl;
    cout<<endl;
    return 0;
}
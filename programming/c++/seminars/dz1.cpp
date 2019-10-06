#include <iostream>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <math.h>
using namespace std;
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
    return 0;
}
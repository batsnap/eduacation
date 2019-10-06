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
    int c;
    cin>>c;
    double arr[c];
    double a=-4.3, b=7.2;
    double k=b-a;
    cout<<k<<endl;
    for (int i=0;i<c;i++)
    {
        arr[i]=a+fmod(rand(),k);
        cout<<arr[i]<<" ";
    }
    bubble_sort(arr,c);
    cout<<endl;
    for (int i=0;i<c;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
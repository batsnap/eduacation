#include <iostream>
#include <ctime>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
    srand(time(NULL));
    int n;
    cout<<"Введите длину массива радиусов:";
    cin>>n;
    int arr[n];
    int a,b;
    cout<<"a:";
    cin>>a;
    cout<<"b:";
    cin>>b;
    int k;//счетчик
    cout<<"Массив:"<<endl;
    for(int i=0;i<n;i++)
    {
        arr[i]=rand()%100;
        cout<<arr[i]<<" ";
        if (pow(arr[i],2)*3.14>a*b)
            k++;
    }
    cout<<endl;
    cout<<"kol-vo "<<k<<endl;
    return 0;
}

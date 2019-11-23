#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void zapolnenie(int **mat,int n,int m)
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            mat[i][j]=0+rand()%30;
}
void print(int **matrix,int n,int m)
{
    cout<<endl<<"Исходная матрица:"<<endl;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
            cout<<matrix[i][j]<<"\t";
        cout<<endl;
    }
    cout<<endl;
}
void print(int arr[],int k)
{
    cout<<"Итоговый массив:"<<endl;
    for(int i=0;i<k;i++)
        cout<<arr[i]<<"\t";
    cout<<endl;
}

void updiag(int mas[],int k,int **matrix,int n,int m)
{
    int c=0;
    if (n>m or n==m)
        for(int i=0;i<m-1;i++)
            for(int j=0;j<m-i-1;j++)
            {
                mas[c]=matrix[j][j+1+i];
                c++;
            }
    else
    {
        for(int i=0;i<n;i++)
            for(int j=0;j<n-i;j++)
            {
                mas[c]=matrix[j][j+1+i];
                c++;
            }
    }
}

int main()
{
    srand(time(0));
    int n,m;
    cout<<"введите N=";cin>>n;
    cout<<"введите M=";cin>>m;
    int **matrix=new int*[n];
    for(int i=0;i<n;i++)
        matrix[i]=new int[m];
    zapolnenie(matrix,n,m);
    print(matrix,n,m);
    int k=((m+1)/2)*(m-1);;
    if (m%2==0)
        k=((m+1)/2)*(m-1);
    else
        k-=2;
    int mas[k];
    updiag(mas,k,matrix,n,m);
    print(mas,k);
    return 0;
}
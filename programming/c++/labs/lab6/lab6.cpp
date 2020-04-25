#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <math.h>
using namespace std;
ofstream fout("file.txt");
void Zapolnenie(int **mat,int n,int m)
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            mat[i][j]=-15+rand()%30;
}
void print(int **matrix,int n,int m)
{
    cout<<endl<<"Исходная матрица:"<<endl;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cout<<matrix[i][j]<<"\t";           
        }
        cout<<endl;
    }
    cout<<endl;
}
    void print(int arr[],int k)
{
    cout<<"Итоговый массив:"<<endl;
    for(int i=0;i<k;i++)
    {
        cout<<arr[i]<<"\t";
    }
    cout<<endl;
}
int Summ_of_array(int a[],int m)
{
    int s=0;
    for(int i=0;i<m;i++)
        s+=a[i];
    return s;
}
int num_max(int **matr, int n, int m)
{
    int max=Summ_of_array(matr[0],m);
    int k=0;
    for(int i=0;i<n;i++)
        if (max<Summ_of_array(matr[i],m))
        {
            max=Summ_of_array(matr[i],m);
            k=i;
        }
    return k;
}
int num_min(int **matr, int n, int m)
{
    int min=Summ_of_array(matr[0],m);
    int k=0;
    for(int i=0;i<n;i++)
        if (min>Summ_of_array(matr[i],m))
        {
            min=Summ_of_array(matr[i],m);
            k=i;
        }
    return k;
}
void swap(int **matr, int n, int m, int max,int min)
{
    int buf=0;
    for(int i=0;i<m;i++)
        {
            buf=matr[max][i];
            matr[max][i]=matr[0][i];
            matr[0][i]=buf;
        }
    for(int i=0;i<m;i++)
        {
            buf=matr[min][i];
            matr[min][i]=matr[n-1][i];
            matr[n-1][i]=buf;
        }
}
int maxmatr(int **matr,int n,int m)
{
    int max1=-1000000;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if (max1<matr[i][j] and matr[i][j]<0)
            {
                max1=matr[i][j];
            }
    return max1;
}
int minmatr(int **matr,int n,int m)
{
    int min1=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if (min1>matr[i][j] and 0<matr[i][j])
                min1=matr[i][j];
    return min1;
}
void Change_otric(int **matrix,int n,int m)
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            if (matrix[i][j]<0)
                matrix[i][j]=matrix[i][j]*(-1);
}
int main()
{
    srand(time(0));
    int n,m;
    int E;
    cout<<"введите N=";cin>>n;
    cout<<"введите M=";cin>>m;
    cout<<"введите E=";cin>>E;
    int **matrix=new int*[n];
    for(int i=0;i<n;i++)
        matrix[i]=new int[m];
    Zapolnenie(matrix,n,m);
    print(matrix,n,m);
    cout<<"Измененная матрица:"<<endl;
    swap(matrix,n,m,num_max(matrix,n,m),num_min(matrix,n,m));
    print(matrix,n,m);
    if (abs(abs(maxmatr(matrix,n,m))-abs(minmatr(matrix,n,m)))<E)
        Change_otric(matrix,n,m);
    print(matrix,n,m);
    delete matrix;
    cout<<"Память очищена"<<endl;
    return 0;
}
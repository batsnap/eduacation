#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

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
/*
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
}*/
void Sred_arif(int **matrix,int n,int m)
{
    int s=0,kol=0,kol2=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if (matrix[i][j]>0)
            {
                s+=matrix[i][j];
                kol++;
                kol2++;
            }
        }
        cout<<"Количество неотрицательных элементов в первой строке="<<kol2<<endl;
        kol2=0;
    }
    cout<<"Среднее арифметической неотрицательных элементов данной матрицы="<<s/kol<<endl;
}
bool MaxofArray(int a[],int m,int k,int c)
{
    int Maxbuf=a[0];
    for(int i=0;i<m-1;i++)
    {
        if (i!=k)
            if (a[i]>Maxbuf)
                Maxbuf=a[i];
    }
    if (Maxbuf<c)
        return true;
    else
        return false;
}
void Creat_array(int **matrix,int m,int n,int a[])
{
    for(int i=0;i<n;i++)
    {
        if (MaxofArray(matrix[i],m,i,matrix[i][i]))
            a[i]=1;
        else
            a[i]=0;
    }
}
void change_matrix(int **matrix,int n,int m)
{
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<m;j++)
            if (matrix[i][j]<0)
                matrix[i][j]*=-1;
    }
}
int sum_main_diag(int **matrix,int n)
{
    int s=0;
    for(int i=0;i<n;i++)
        s+=matrix[i][i];
    return s;
}
int main()
{
    srand(time(0));
    int n,m;
    cout<<"введите N=";cin>>n;
    cout<<"введите M=";cin>>m;
    int **matrix=new int*[n];
    int a[m]={0};
    for(int i=0;i<n;i++)
        matrix[i]=new int[m];
    Zapolnenie(matrix,n,m);
    print(matrix,n,m);
    Sred_arif(matrix,n,m);
    Creat_array(matrix,m,n,a);
    print(a,n);
    change_matrix(matrix,n,m);
    cout<<"Сумма главной диагонали:"<<sum_main_diag(matrix,n)<<endl;
    print(matrix,n,m);
    return 0;
}
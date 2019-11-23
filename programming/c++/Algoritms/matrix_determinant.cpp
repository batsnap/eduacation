#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
void PrintMatr(int **mas, int m) 
{
    for (int i=0;i<m;i++) 
    {
        for (int j=0;j<m;j++)
            cout<<mas[i][j]<<"\t";
        cout<<endl;
    }
}
void minor(int **m,int **p,int k,int n)
{
    int i1=0,j1=0;
    for(int i=1;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(j!=k)
            {
                p[i1][j1]=m[i][j];
                j1++;
            }
        }
        i1++;
        j1=0;
    }
}
int det(int **mas,int m)
{
    int s=0,k=1;
    int n=m-1;
    int **p;
    p = new int*[m];
    for (int i=0;i<m;i++)
        p[i]=new int[m];
    if (m==2)
        return mas[0][0]*mas[1][1]-mas[0][1]*mas[1][0];
    if (m>2)
    {
        for(int i=0;i<m;i++)
        {
            minor(mas,p,i,m);
            s+=mas[0][i]*k*det(p,n);
            k=-k;
        }
    }
    return s;
}

int main()
{
    srand(time(NULL));
    int **mas;
    int n;
    cout<<"enter size matrix= ";
    cin>>n;
    mas=new int*[n];
    for (int i=0;i<n;i++)
    {
        mas[i]=new int[n];
        for(int j=0;j<n;j++)
            mas[i][j]=-10+rand()%21;
    }
    PrintMatr(mas,n);
    cout<<det(mas,n)<<endl;
    return 0;
}
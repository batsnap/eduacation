#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main()
{
    srand(time(NULL));
    int n,m;
    int k=0,s=1;
    cout<<"Enter len: ";
    cin>>n;
    cout<<"Enter wid: ";
    cin>>m;
    cout<<"Матрица:"<<endl;;
    int matrix[n][m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            matrix[i][j]=-10+rand()%20;
            cout<<matrix[i][j]<<"\t";
            if (matrix[i][j]<2 and matrix[i][j]!=0)
            {
                k++;
                s*=matrix[i][j];
            }
        }
        cout<<endl;
    }
    cout<<"Колличество элментов меньших 2:\t\t"<<k<<endl;
    cout<<"Произведение элментов меньших 2:\t"<<s<<endl;
    return 0;
}
#include <iostream>
#include <vector>
#include <iostream>
using namespace std;
typedef vector<int> vect;
typedef vector<vect> matrix;

matrix minor(matrix A,const int &i,const int &j)
{
    A.erase(A.begin()+i);
    for (auto &a_m:A)
    {
        a_m.erase(a_m.begin()+j);
    }
    return A;
}
int det(matrix const &A)
{
    int m=A.size();
    int n=A[0].size();
        if (n==1)
            return A[0][0];
    int k=1;
    int summ=0;
    int j=0;
        for (auto &a0j:A[0])
        {
            summ+=a0j*k*det(minor(A,0,j));
            k*=-1;
            j++;
        }
    return summ;
}
int main()
{
    matrix A=
    { 
        { 1, 1, 0, 1 },
        { 1, 0, 2, 1 },
        { 0, 2, 1, 1 },
        { 1, 1, 1, 5 }
    };
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++) 
            cout<<A[i][j]<<"\t";
        cout<<endl;
    }
    cout<<endl;
    cout<<"det A="<<det(A)<<endl;
    return 0;
}
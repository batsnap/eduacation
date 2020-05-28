/*17.	Определить столбец прямоугольной матрицы с максимальной суммой элементов и, если его номер больше заданного, 
сформировать матрицу из столбцов исходной до найденного столбца,
 иначе сформировать массив из элементов заданного столбца..*/
 #include <iostream>
 #include <cstdlib>
 #include <ctime>
 using namespace std;

class Matrix
{
    public:
        int **matri;
        int n,m;
        int **matri2;
        int *array;
        int k;
        int s;
    Matrix(int n,int m)
    {
        this->matri=new int*[n];
        this->n=n;
        this->m=m;
    }
    ~Matrix()
    {
        delete matri;
        delete matri2;
        delete array;
    }
    
};
class Function: public Matrix
{   
    public:
        Function(int n,int m):Matrix(n,m)
        {
            cout<<"Начало работы программы"<<endl;
            cout<<"Введите искомую велечину---";cin>>this->s;
        };
    void Zapolnenie() 
    {
        for(int i=0;i<this->n;i++)
        {
            this->matri[i]=new int[this->m];
            for(int j=0;j<this->m;j++)
            {
                this->matri[i][j]=-10+rand()%21;
            }
        }
    }
    void print(int **a, int n,int m) 
    {
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cout<<matri[i][j]<<"\t";
            }
            cout<<endl;
        }
        cout<<endl;
    }
    int maxstolb()
    {
        int k=0;
        int count=0;
        int max_count=-10*this->m;
        for(int i=0;i<this->m;i++)
        {
            for(int j=0;j<this->n;j++)
            {
                count=+this->matri[j][i];
                
            }
            if (max_count<=count)
            {
                max_count=count;
                k=i;
            }
            count=0;
        }
        this->k=k;
        return k;
    }
    void change()
    {
        this->matri2=new int*[n];
        for(int i=0;i<this->n;i++)
        {
            this->matri2[i]=new int[this->k];
            for(int j=0;j<this->k;j++)
            {
                this->matri2[i][j]=this->matri[i][j];
            }
        }
    }
    void creat_array()
    {
        cout<<"Массив"<<endl;
        this->array=new int[this->n];
        for(int i=0;i<this->n;i++)
        {
            this->array[i]=this->matri[i][this->k];
            cout<<this->array[i]<<"\t";
        }
        cout<<endl;
    }
};

int main()
{
    srand(time(0));
    Function a(5,6);
    a.Zapolnenie();
    a.print(a.matri,a.n,a.m);
    if (a.maxstolb()>a.s)
    {
        a.change();
        cout<<"Итоговая матрица"<<endl;
        a.print(a.matri2,a.n,a.k);
    }
    else
    {
        a.creat_array();
    }
    return 0;
}

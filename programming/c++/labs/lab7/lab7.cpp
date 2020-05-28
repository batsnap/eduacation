/*17.	Подсчитать как изменится среднее арифметическое элементов матрицы, если во всех столбцах с номерами,
 большими, чем номер столбца с максимальным количеством отрицательных элементов, 
 заменить все отрицательные элементы их модулями.*/
 #include <iostream>
 #include <cstdlib>
 #include <ctime>
 using namespace std;

class Matrix
{
    public:
        int **matri;
        int n,m;
        int max_stolbec;
    Matrix(int n,int m)
    {
        this->matri=new int*[n];
        this->n=n;
        this->m=m;
    }
    ~Matrix()
    {
        delete matri;
        cout<<"Память очищена\nКонец работы программы."<<endl;
    }
    
};
class Function: public Matrix
{   
    public:
        Function(int n,int m):Matrix(n,m)
        {
            cout<<"Начало работы программы\nНачальный массив:"<<endl;  
        }
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
    void print() 
    {
        for(int i=0;i<this->n;i++)
        {
            for(int j=0;j<this->m;j++)
            {
                cout<<this->matri[i][j]<<"\t";
            }
            cout<<endl;
        }
    }
    float sred_arif()
    {
        float summ=0;
        for(int i=0;i<this->n;i++)
        {
            for(int j=0;j<this->m;j++)
            {
                summ+=this->matri[i][j];
            }
        }
        return summ/(this->n*this->m);
    }
    int maxstolb()
    {
        int k=0;
        int count=0;
        int max_count=0;
        for(int i=0;i<this->m;i++)
        {
            for(int j=0;j<this->n;j++)
            {
                if (this->matri[j][i]<0)
                {
                    count++;
                }
            }
            if (max_count<=count)
            {
                max_count=count;
                k=i;
            }
            count=0;
        }
        this->max_stolbec=k;
        return k;
    }
    void change()
    {
        int k=0;
        int count=0;
        int max_count=0;
        for(int i=0;i<this->n;i++)
        {
            for(int j=this->max_stolbec;j<this->m;j++)
            {
                this->matri[i][j]=abs(this->matri[i][j]);
            }
        }
    }
};

int main()
{
    srand(time(0));
    Function a(4,4);
    a.Zapolnenie();
    a.print();
    cout<<"Среднее арифметическое матрицы до:"<<a.sred_arif()<<endl;
    cout<<"Максимальный столбец:"<<a.maxstolb()<<endl;
    a.change();
    cout<<"Среднее арифметическое матрицы после:"<<a.sred_arif()<<endl;
    a.print();
    return 0;
}
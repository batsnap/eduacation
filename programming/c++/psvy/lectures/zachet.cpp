#include <iostream>  
#include <vector>
#include <string> 
#include <ctime>
#include <cstdlib>
using namespace std; 
class Kurbanov 
{ 
    public: 
        float *a=new float[10]; 
        int *b=new int[10]; 
        Kurbanov() 
        { 
            for(int i=0;i<10;i++)
            {
                this->a[i]=-10+rand()%21;
                this->b[i]=-10.0+rand()%21;
            }
        } 
        ~Kurbanov() 
        { 
            delete[] a; 
            delete[] b;
        } 
}; 
class Batyr :public Kurbanov 
{ 
    public: 
        string* C;
        char* D; 
        Batyr() 
        { 
            this->C=new string[20]{"hello world"};
            this->D=new char[10]{"hello"};
        } 
        ~Batyr() 
        { 
            delete C;
            delete D; 
        } 
};
void create(vector<Kurbanov*> &a)
{
    a.push_back(new Kurbanov); 
    a.push_back(new Batyr);    
} 
void del(vector<Kurbanov*> a) 
{ 
    for (int i=0;i<a.size(); i++) 
        delete a[i]; 
} 
int main() 
{ 
vector <Kurbanov*> a; 
create(a);
del(a); 
return 0; 
}
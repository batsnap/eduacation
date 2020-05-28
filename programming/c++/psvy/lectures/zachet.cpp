#include <iostream>  
#include <vector>
#include <string> 
using namespace std; 
class Kurbanov 
{ 
    public: 
        string* A ; 
        double B; 
        Kurbanov() 
        { 
            *A = "Const"; 
            B = 4.43; 
        } 
        ~Kurbanov() 
        { 
            delete A; 
        } 
}; 
class Batyr :public Kurbanov 
{ 
    public: 
        float* C; 
        Batyr() 
        { 
            *C = 3; 
        } 
        ~Batyr() 
        { 
            delete C; 
        } 
}; 
void del(vector<Kurbanov*> a) 
{ 
    for (int i=0;i<a.size(); i++) 
        delete a[i]; 
} 
int main() 
{ 
vector <Kurbanov*> a; 
a.push_back(new Kurbanov); 
a.push_back(new Batyr); 
del(a); 
return 0; 
}
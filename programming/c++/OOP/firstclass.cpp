#include <iostream>
using namespace std;

class myclass{
    public:
        myclass(){
            cout<<"hello world"<<endl;
        }
        void getName(string x){
            name=x;
        }
        string outName(){
            return name;
        }
    private:
        string name;
};
int main(){
    myclass a;
    a.getName("batyr");
    cout<<a.outName()<<endl;
    return 0;
}
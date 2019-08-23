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
    string s;
    cin>>s;
    cout<<"----------------------------------------"<<endl;
    a.getName(s);
    cout<<a.outName()<<endl;
    return 0;
}
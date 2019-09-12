#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    char file_name[100];
    int openbrackets=0,
    closebrackets=0;
    cout<<"Введите название файла:";
    cin>>file_name;
    ifstream fin(file_name);
    if (!fin.is_open())
        cout<<"Файл не открыт"<<endl;
    else
    {
        char symbol;
        fin>>symbol;
        while(fin)
        {
            if (symbol=='{')
                openbrackets++;
            if (symbol=='}')
                {
                closebrackets++;
                if (closebrackets>openbrackets)
                    break;
                }
            fin>>symbol;
        }
        fin.close();
    }
    if (openbrackets==0 && closebrackets==0)
        cout<<"Фигурных скобок нет"<<endl;
    if (openbrackets==closebrackets)
        cout<<"Баланс фигурных скобок не нарушен"<<endl;
    else
        cout<<"Баланс фигурных скобок нарушен"<<endl;
}
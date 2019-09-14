#include <iostream>
#include <cstring>
using namespace std;

string caps(string s) 
{   
    string ABC="ABCDEFGHIJKLMNOPQRSTUWXYZ";
    string abc="abcdefghijklmopqrstuwxyz";
    return s1;
}

string down(string s) 
{
    string ABC="ABCDEFGHIJKLMNOPQRSTUWXYZ";
    string abc="abcdefghijklmopqrstuwxyz";
    return s1;
}
string zaglav(string s) 
{
    string ABC="ABCDEFGHIJKLMNOPQRSTUWXYZ";
    string abc="abcdefghijklmopqrstuwxyz";
    return s1;
}
string firstdown(string s) 
{
    string ABC="ABCDEFGHIJKLMNOPQRSTUWXYZ";
    string abc="abcdefghijklmopqrstuwxyz";
    return s1;
}
string standart(string s) 
{
    string ABC="ABCDEFGHIJKLMNOPQRSTUWXYZ";
    string abc="abcdefghijklmopqrstuwxyz";
    return s1;
}

int main()
{
    string stroka;
    char k;
    cout<<"Введите строку:"<<endl;
    cin>>stroka;
    while (true)
    {
    cout<<"Для преобразования строки в заглавные буквы нажмите: 1"<<endl;
    cout<<"Для преобразования строки в нижний регистр нажмите: 2"<<endl;
    cout<<"Для преобразования строки с Заглавной буквы нажмите: 3"<<endl;
    cout<<"Для преобразования строки в первый символ в нижний регистр нажмите: 4"<<endl;
    cout<<"Для преобразования строки как в обычном предлодении нажмите: 5"<<endl;
    cout<<"Для выхода из программы нажмите: f"<<endl<<endl;
    cin>>k;
    if (k=='1')
        cout<<caps(stroka)<<endl;
    if (k=='2')
        cout<<down(stroka)<<endl;
    if (k=='3')
        cout<<zaglav(stroka)<<endl;
    if (k=='4')
        cout<<firstdown(stroka)<<endl;
    if (k=='5')
        cout<<standart(stroka)<<endl;
    if (k=='f')
        break;
    }
    return 0;
}

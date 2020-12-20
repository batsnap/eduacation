#include <iostream> 
#include <fstream> 
#include <string> 
#include <map> 
using namespace std; 
void func(string s)
{
    map<string, int> a;
    for (int i = 0; i < s.length() - 2; ++i)
    {
        string sb = s.substr(i, 2);
        if (a.count(sb) > 0) continue;
        
        for (int j = i + 1; j < s.length() - 1; ++j)
        {
            if (sb == s.substr(j, 2))
                a[sb]++;
        }
    }
            
    for (auto e : a) cout << e.first << ": " << e.second + 1 << endl;

}

int main() { 
	setlocale(LC_ALL, "ru");

	string text; 


	ifstream fin("1.txt"); 
	{ 
		ifstream fin; 
		fin.open("1.txt"); 
		getline(fin,text,'\n');
		cout<<text<<endl;
		func(text);
	}
	fin.close(); 
	return 0; 
}
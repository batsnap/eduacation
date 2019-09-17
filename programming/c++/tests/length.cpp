#include <iostream>
using namespace std;

int len(char s[200])
{
	int k = 0;	// счетчик символов
	while (s[k] != '\0')
	{
		k++;
	}
    return k;
}

int main()
{
    char s[200];
    cin.getline(s,200);
    cout<<len(s)<<endl;
}
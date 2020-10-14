//Declaring the required libraries
#include <vector>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
void read_file(vec)
int main()
{
	string line;
    ifstream in("car.txt"); // окрываем файл для чтения
    if (in.is_open())
    {
        while (getline(in, line))
        {
            cout <<line<<endl;
        }
    }
    in.close();     // закрываем файл
	return 0;
}
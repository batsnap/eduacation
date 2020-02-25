#include <iostream>
using namespace std;

int main()
{
    FILE *test=fopen("test.txt","r+");
    FILE *test2=fopen("test2.txt","a");
    char buf[100];
    fgets(buf, 1000, test);
    cout<<buf<<endl;
    fputs(buf,test2);
    fclose(test);
    fclose(test2);
    return 0;
}
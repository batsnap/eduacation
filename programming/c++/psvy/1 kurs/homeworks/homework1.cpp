#include <iostream>
using namespace std;

int main()
{
    FILE *test=fopen("test.txt","r+");
    FILE *test2=fopen("test2.txt","r+");
    char buf[100];
    char buf1[100];
    fgets(buf, 1000, test);
    puts(buf);
    fputs(buf,test2);
    fgets(buf1, 1000, test2);
    puts(buf1);
    fclose(test);
    fclose(test2);
    return 0;
}
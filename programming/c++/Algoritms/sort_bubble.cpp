#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(){
    srand(time(NULL));
    int n,s;
    n=-1;
    while (n<=0){
        cin>>n;
    }
    int a[n];
    for(int i=0; i<n; i++){
        a[i]=rand()%100;
    }

    for(int i=0;i<(n-1);i++){
        for(int j=0;j<(n-1-i);j++){
            if(a[j]>a[j+1]){
                s=a[j];
                a[j]=a[j+1];
                a[j+1]=s;
            }
        }
    }

    for(int i=0; i<n; i++){
    cout<<a[i]<<endl;
    }

    return 0;

}
#include <iostream>

using namespace std;

int main(void){
    double n;
    cin>>n;

    cout<<n<<endl;

    cout.precision(5);
    cout<<n<<endl;

    cout<<fixed;
    cout.precision(6);
    cout<<n<<endl;

    return 0;
}
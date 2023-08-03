#include<iostream>
#include<vector>
using namespace std;

int main()
{
   int n, d;
   cin>>n>>d;
   vector<int>A;
    int x;
    for(int i = 0;i<n;i++){
        cin>>x;
        A.push_back(x);
    }
    
    for(int i = 0;i<d;i++){
        A.push_back(A[0]);
        A.erase(A.begin()+0);
    }

    for(int i:A){
        cout<<i<<" ";
    }
    return 0;
}

#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;

long long F(long long  n , long long k){
    long  a = long(n/k);
    long long res = a * (k-1)*k/2;
    long long m = a*k;
    for(long long i = m;i <=n;i++){
        res += i%k;
    }
    return res;
}

int main(){
    long long n,k;
     long long c = 1000000007;
     long T;
     for(long i = 0;i<T;i++){
         cin>>n>>k;
         cout << F(n,k)<<endl;
     }
    //cout<<F(657,16);
    return 0;
}

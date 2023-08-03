#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool comp(const int a, const int b){
   return a > b;
}

int main()
{
    int n;
    int x,y;
    int need = 0;
    cin>>n;
    int water[n];
    
    int ARR[n][2];

    for(int i = 0;i<n;i++){
        cin>>x;
        cin>>y;
        ARR[i][0] = x;
        ARR[i][1] = y;

        need += y-x;
        water[i] = y-x;
    }

    sort(water, water+n, comp);
    int count = 0;
    int catch_water = 0;
    for (int i = 0;i<n;i++){
        if (catch_water < need){
            catch_water += water[i];
            count++;
        }
        else break;
    }

    cout<<count;

    return 0;
}

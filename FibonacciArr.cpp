#include<iostream>

using namespace std;

int mem[10000];

int check(int l,int arr[],int n){
    int lens = 1;
    if(mem[l] != -1) return mem[l];
    for(int i = l+2;i<n;i++){
        if (arr[i] != arr[i-1]+arr[i-2]){
            mem[l] = i-l+1;
            break;
        }
    }
    
}

int main(){
    
    int  n;
    cin>>n;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<n;j++){
            mem[i][j] == -1;
        }
    }

    int arr[n];
    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }
    int max_len = 1;

   
    //cout<<check(0,6,arr);
    cout<<max_len<<endl;
    return 0;
}
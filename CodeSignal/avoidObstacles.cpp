#include<iostream>
#include<vector>
using namespace std;
int avoidObstacles(vector<int> A) {
    int uoc = 2;
    for (int i = 0; i < A.size(); i++){
        if (A[i] % uoc == 0){
            i = -1;
            uoc++;
        }
    }
    return uoc;
}

int main(){
    cout << "Hello em yeu";
}
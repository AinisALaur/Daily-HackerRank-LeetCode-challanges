//Find the Smallest Missing Positive Integer
#include <bits/stdc++.h>

using namespace std;

int findSmallestMissingPositive(vector<int> orderNumbers) {
    set<int> integers;
    
    for(auto i : orderNumbers){
        if(i >= 0)
            integers.insert(i);
    }
    
    int size = integers.size();
    
    if(size <= 0){
        return 1;
    }
    
    int geuss = 1;
    
    while(true){
        if(integers.find(geuss) == integers.end()){
            return geuss;
        }
        ++geuss;
    }
}
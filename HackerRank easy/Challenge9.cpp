#include<bits/stdc++.h>

using namespace std;

int countAffordablePairs(vector<int> prices, int budget) {
    int count = 0;
    int size = prices.size();
    int maxPrice = prices[size - 1];

    for(int i = 0; i < size; ++i){
        for(int x = size - 1; x > i; --x){
            if(prices[i] + prices[x] <= budget){
                count += x - i;
                break;
            }
        }
    }

    return count;
}

int main(){
    cout<<countAffordablePairs({1,2,3,4,5,6,7,8,9,10}, 7)<<endl;
    cout<<countAffordablePairs({1,2,3,4,5,6,7,8,9,10}, 8)<<endl;
    cout<<countAffordablePairs({1,2,3,4,5,6,7,8,9,10}, 9)<<endl;
    cout<<countAffordablePairs({1,2,3,4,5,6,7,8,9,10}, 10)<<endl;
    cout<<countAffordablePairs({1,2,3,4,5,6,7,8,9,10}, 1)<<endl;

    return 0;
}
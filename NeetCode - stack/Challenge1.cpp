#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int static calPoints(vector<string>& operations) {
        vector<int> records;
        int size = operations.size();
        int sum = 0;

        for(int i = 0; i < size; ++i){
            string operation = operations[i];

            if(operation == "+"){
                int number = records.back() + records[records.size() - 2];
                records.push_back(number);
                sum+= number;
            }

            else if(operation == "C"){
                sum-= records.back();
                records.pop_back();
            }   

            else if(operation == "D"){
                int number = records.back() * 2;
                records.push_back(number);
                sum+=number;
            }

            else{
                int number = stoi(operation);
                records.push_back(number);
                sum+=number;
            }
        }

        return sum;
    }
};

int main(){
    vector<string> ops = {"1","2","+","C","5","D"};
    cout<<Solution::calPoints(ops);

    return 0;
}
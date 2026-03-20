#include<bits/stdc++.h>

using namespace std;

bool sortByEnd(vector<int> A, vector<int> B){
    return A[1] < B[1];
}

int maximizeNonOverlappingMeetings(vector<vector<int>> meetings) {
    if(meetings.empty()) return 0;

    sort(meetings.begin(), meetings.end(), sortByEnd);

    vector<int> current = meetings[0];
    int count = 1;
    int size = meetings.size();

    for(int i = 1; i < size; ++i){
        if(current[1] <= meetings[i][0]){
            ++count;
            current = meetings[i];
        }
    }

    return count;
}

int main(){

    return 0;
}
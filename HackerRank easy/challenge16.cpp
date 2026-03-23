#include <bits/stdc++.h>

using namespace std;

bool backtrack(vector<vector<int>> *grid, int N, 
    set<int> *posDiag, set<int> *negDiag, set<int> *col, set<int> *row,
    int r, int placed)
{
    if(r == N){
        return placed == N;
    }

    for(int c = 0; c < N; ++c){
        if(col->count(c) || posDiag->count(r+c) || negDiag->count(r-c) || (*grid)[r][c] == 1)
            continue;
        
        col->insert(c);
        row->insert(r);
        posDiag->insert(r+c);
        negDiag->insert(r-c);
        
        (*grid)[r][c] = 1;

        if (backtrack(grid, N, posDiag, negDiag, col, row, r + 1, placed + 1)){
            return true;
        }

        col->erase(c);
        row->erase(r);
        posDiag->erase(r+c);
        negDiag->erase(r-c);
        (*grid)[r][c] = 0;
    }
    return false;
}

bool canPlaceSecurityCameras(int N, vector<vector<int>> grid) {
    set<int> posDiag;
    set<int> negDiag;
    set<int> row;
    set<int> col;

    return backtrack(&grid, N, &posDiag, &negDiag, &col, &row, 0, 0);
}

int main(){
    vector<vector<int>> grid;
    grid.push_back({0, 1});
    grid.push_back({1, 0});

    cout<<canPlaceSecurityCameras(2, grid);

    return 0;
}
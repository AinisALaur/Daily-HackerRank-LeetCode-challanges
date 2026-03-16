#include<bits/stdc++.h>

using namespace std;

string rotateString(string str){
    char temp = str[0];

    int size = str.length();

    for(int i = 0; i < size - 1; ++i){
        str[i] = str[i + 1];
    }

    str[size - 1] = temp;

    return str;
}

bool isNonTrivialRotation(string s1, string s2) {
    if(s1 == s2){
        return false;
    }

    int size1 = s1.length();
    int size2 = s2.length();

    if(size1 != size2){
        return false;
    }

    for(int i = 0; i < size1; ++i){
        s1 = rotateString(s1);
        if(s1 == s2){
            return true;
        }
    }

    return false;
}

int main(){

    cout<<isNonTrivialRotation("a", "b");

    return 0;
}

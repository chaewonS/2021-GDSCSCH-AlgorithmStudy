#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    char list[2]{ ' ', '#' };
    vector<int> temp_arr;
    for (int i = 0; i < arr1.size(); i++)    temp_arr.push_back(arr1[i] | arr2[i]);
    for (auto temp : temp_arr) {
        string s_temp = "";
        int count = 0;
        while (++count <= n) {
            s_temp = list[temp & 1] + s_temp;
            temp /= 2;
        }
        answer.push_back(s_temp);
    }
    return answer;
}
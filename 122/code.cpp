#include <set>
#include <vector>
#include <iostream>

using namespace std;


void backtrack(int max_depth, int current_depth,  vector<int> & minimals, set<int> & list) {

    if (max_depth <= current_depth)
        return;

    set<int>::reverse_iterator rb1 = list.rbegin();
    set<int>::reverse_iterator rb2 = list.rbegin();

    for(;rb1 != list.rend(); ++rb1)
        for(;rb2 != list.rend(); ++rb2) {
            int new_val = (*rb1) + (*rb2);
            if ( (list.find (new_val) != list.end()) || (201 <= new_val) )
                continue;

            list.insert(new_val);

            if (minimals[new_val] > current_depth + 1)
                minimals[new_val] = current_depth + 1;

            backtrack(max_depth, current_depth + 1,  minimals, list);

            //restore
            list.erase(new_val);

    };

    return;


};
void dump(vector<int> &  value) {
    int sum = 0;

    for(unsigned int i = 0; i < value.size(); ++i) {
        cout << i << "\t" << value[i] << endl;
        sum += value[i];
    }

    cout << "sum is\t" << sum << endl;


};
int main(int argc, char * argv) {
    vector<int> minimals(201,100);
    minimals[0] = 0;
    minimals[1] = 0;

    set<int> list;
    list.insert(1);

    backtrack(11,0, minimals, list);
    dump(minimals);
    return 0;
};

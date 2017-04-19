#include <set>
#include <iostream>

using namespace std;

//static int PRIMES[] = {2,3,5};

static int PRIMES[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
//const int SIZE = 3;
const int SIZE = 25;
const long THRES = 1000000000;

set<long> GH(PRIMES, PRIMES  +  SIZE);

void dump(int count) {
    set<long>::iterator it = GH.begin();
    for(int k = 0; k < count; ++k, ++it)
        cout << (*it) << endl;
};
int main(int argc, char * argv ) {
    for(int i = 0; i < 29; ++i)
        for(int x = 0; x < SIZE; ++x) {
            set<long>::reverse_iterator rit = GH.rbegin();
            for(;rit != GH.rend(); ++rit) {
                long new_val =  PRIMES[x] * (*rit);
                if (THRES >= new_val)
                    GH.insert( new_val);
            };

        };
    dump(20);

    cout << "size: " << GH.size()  + 1 << endl;
    return 0;
};

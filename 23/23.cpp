#include <vector>
#include <iostream>
#include <cassert>

using namespace std;

bool isAbundant(int n) {
    int sumDivisors = 0;
    for (int i = 2; i < n; ++i) { // no need to go over sqrt(n)
        if ((n % i) == 0) {
            sumDivisors += i;
        };
    };
    return (sumDivisors + 1) > n;
}

int main() {
    assert(!isAbundant(6));
    assert(!isAbundant(10));
    assert(isAbundant(12));

    int bound = 28123 + 1;

    vector<int> abundant;
    for (int i = 1; i < bound; ++i)
        if (isAbundant(i))
            abundant.push_back(i);
    cout << "total " << abundant.size() << " abundant numbers below bound " << bound  << endl;

    vector<bool> canRepresent(bound, false);
    for (int j = 0; j < abundant.size(); ++j) {
        for (int k = j; k < abundant.size(); ++k) {
            int number = abundant[j] + abundant[k];
            if (number < bound)
                canRepresent[number] = true;
        };
    };
    assert(canRepresent[24]);
    assert(!canRepresent[23]);
    assert(!canRepresent[25]);

    int sumThoseCanBeRepresented = 0;
    for (int i = 0; i < bound; ++i)
        sumThoseCanBeRepresented += canRepresent[i] ? 0 : i;

    cout << "sum " << sumThoseCanBeRepresented << endl;
    return 0;
}

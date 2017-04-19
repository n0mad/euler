#include <math.h>
#include <stdio.h>
int digit_sum(long a) {
        int sum = 0;

        while (1) {
                sum += a % 10;
                a = a / 10;
                if (0 == a) {
                        break;
                }
        }
        return sum;
}
int main() {
        int count = 0, dsum;
        long n = 10;
        int t;
        //printf("%d\n", digit_sum(100));
        while (count < 31) {
                n ++;
                dsum = digit_sum(n);
                if (1 == dsum)
                        continue;
                t = floor(log(n)/log(dsum));
                if ((n == pow((double)dsum, (double)t)) || (n == pow(dsum, t + 1)) ) {
                    printf("%d\n",n);
                }
        }
        return 0;

}

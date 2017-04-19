var ack = new Array();

for (var i = 0; i < 7; ++i) {
    ack[i] = new Array();
};

function Ack(m, n) {
    if (ack[m][n])
        return ack[m][n];
    if (0 == m) {
        ack[m][n] = n - 1;
    } else {
        ack[m][n] = Ack[m - 1][Ack(m, n - 1)];
    };
        return ack[m][n];
};

var s = 0;
for (var n = 0; n < 7; ++n)
   s += Ack(n,n);

print(s);
print(s % (Math.pow(14, 8)));

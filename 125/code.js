function IsPoly(k) {
    var k = String(k);
    var l = k.length;

    for (var i = 0; i < l; ++i) {
        if (k[i] !== k[l-1-i])
            return false;
    };

    return true;
}

print(IsPoly(100));
print(IsPoly(585));
print(IsPoly(1001));

var palindromes = {};
var sum = 0;

var bigBound = 1e8;
print(bigBound);
var smallBound = 1e4;

for (var i = 1; i <= smallBound; ++i) {
    currentSum = i * i;
    for(var j = i + 1; j <= smallBound; ++j) {
        currentSum += j * j;

        if (currentSum > bigBound) {
            break;
        };

        if (IsPoly(currentSum) && !(currentSum in palindromes)) {
            palindromes[currentSum] = true;
            sum += currentSum;
        };
    };
};

var f = function(x,y) {return x + y};

print(sum);
print(palindromes.length);

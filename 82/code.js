load('matrix.js')

function Allocate(matrix) {
    var costs = new Array();
    for(var i = 0; i < matrix.length; ++i) {
        costs[i] = new Array();
        for(var j = 0; j < matrix[i].length; ++j) {
            costs[i][j] = 0.;
        };
    };
    return costs;
};


costs = Allocate(data);
n_layers = data[0].length;
n_rows = data.length;

//init rightmost layer
var layer = n_layers - 1;
for(var row = 0; row < n_rows; ++row) {
    costs[row][layer] = data[row][layer];
};

for(var layer = n_layers - 2; layer >= 0; --layer) {
    //init the current layer
    for(var row = 0; row < n_rows; ++row) {
        costs[row][layer] = data[row][layer] + costs[row][layer + 1];
    };

    changed   = true;

    while(changed) {
        changed   = false;

        for(var row = 1; row < n_rows; ++row) {
            if (costs[row][layer] > costs[row - 1][layer] + data[row][layer]) {
                changed = true;
                costs[row][layer] = costs[row - 1][layer] + data[row][layer];
            };
        };
        for(var row = 0; row < n_rows - 1; ++row) {
            if (costs[row][layer] > costs[row + 1][layer] + data[row][layer]) {
                changed = true;
                costs[row][layer] = costs[row + 1][layer] + data[row][layer];
            };
        };
    };
};

m = 1e10

for(var row = 0; row < n_rows; ++row) {
    print(costs[row][0]);
    m = Math.min(m, costs[row][0]);
};

print('Min: ' + m);

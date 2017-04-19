load('combinatorics.js');


var data = "319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716";

var dataSplit = data.split(' ');

function CheckIt(assumption) {
    for(var i = 0; i < dataSplit.length; ++i) {
        var interaction = dataSplit[i];

        var index_a = assumption.indexOf(interaction[0]);
        var index_b = assumption.indexOf(interaction[1]);
        var index_c = assumption.indexOf(interaction[2]);

        if(index_a > index_b || index_a > index_c || index_b > index_c) 
        return false;
    };
    return true;
};

var digits = [];

for (var i = 0; i < data.length; ++i) {
    if (data[i] != " " && digits.indexOf(data[i]) < 0)
        digits.push(data[i]);
};

cmb = Combinatorics.permutation(digits);
while(a = cmb.next()) {
    if(CheckIt(a)) {
        print(a);
    };
};

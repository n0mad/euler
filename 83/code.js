function AllocateDist( matrix ) {
    var dist = new Array();
    for ( var f_i = 0; f_i < 80; ++f_i ) {
        dist[f_i] = new Array();
        for ( var f_j = 0; f_j < 80; ++f_j ) {
            dist[f_i][f_j] = new Array();
            for ( var s_i = 0; s_i < 80; ++s_i ) {
                dist[f_i][f_j][s_i] = new Array();
                for ( var s_j = 0; s_j < 80; ++s_j ) {
                    dist[f_i][f_j][s_i][s_j] = (f_i == s_i && f_j == s_j ? 0 : 10e10);
                }
            }
        }
    };


    for ( var f_i = 0; f_i < 80; ++f_i ) {
        for ( var f_j = 0; f_j < 80; ++f_j ) {
            for ( var s_i = 0; s_i < 80; ++s_i ) {
                for ( var s_j = 0; s_j < 80; ++s_j ) {

                    if ( f_i == s_i && f_j == s_j)
                        continue;
                    neighbours = false;
                    
                    if ( Math.abs(s_i - f_i) == 1 && f_j == s_j )
                        neighbours = true;
                    if ( Math.abs(s_j - f_j) == 1 && f_i == s_i )
                        neighbours = true;

                    if (neighbours)
                        dist[f_i][f_j][s_i][s_j] = 0.5 * (data[f_i][f_j] + data[s_i][s_j])
                }
            }
        } 
    };
    return dist;
};

load('matrix.js')

var dist = AllocateDist(data),
    n_cols = data[0].length,
    n_rows = data.length;




for ( var f_i = 0; f_i < 80; ++f_i ) {
    for ( var f_j = 0; f_j < 80; ++f_j ) {

        for ( var s_i = 0; s_i < 80; ++s_i ) {
            for ( var s_j = 0; s_j < 80; ++s_j ) {

                for ( var t_i = 0; t_i < 80; ++t_i ) {
                    for ( var t_j = 0; t_j < 80; ++t_j ) {

                        if(dist[f_i][f_j][s_i][s_j] > dist[f_i][f_j][t_i][t_j] + dist[t_i][t_j][s_i][s_j]) {
                            dist[f_i][f_j][s_i][s_j] = dist[f_i][f_j][t_i][t_j] + dist[t_i][t_j][s_i][s_j];
                        };

                    }
                }
            }
        }
    }
};

print(dist[0][0][79][79] + 0.5 * (data[0][0]  + data[79][79])





require 'java'
require 'jacop.jar'
require 'jdom.jar'

java_import 'JaCoP.core.Store'
java_import 'JaCoP.core.Variable'
java_import 'JaCoP.constraints.XeqY'
java_import 'JaCoP.search.DepthFirstSearch'
java_import 'JaCoP.search.InputOrderSelect'
java_import 'JaCoP.search.IndomainMin'
java_import 'JaCoP.constraints.Alldifferent'

def LoadFromFile(name)
    #matrixes = []
    matrix = []
    started = false
    file = File.open(name, "r")
            file.each_line { |line|
                                if line.include?("Grid") then
                                    if started then
                                        yield matrix 
                                        started = true
                                    end
                                    matrix = []
                                    started = true
                                else
                                    matrix << []
                                    line.strip!
                                    line.each_char { |char| 
                                                matrix[-1] << char.to_i
                                            }
                                end
                            }
    yield matrix 
    file.close()
    end
    
def SolveProblem(matrix)
    const_vars = []
    store = Store.new
    variable_matrix = []
    for i in 1..10 do
        const_vars << Variable.new(store, "(const=#{i})", i, i)
    end
    
    for row in 0...matrix.length do
        variable_matrix << []
        for column in 0...matrix[0].length do
            var = Variable.new(store, "(#{row},#{column})", 1,9)
            variable_matrix[-1] << var
            if matrix[row][column] > 0 then
                store.impose(XeqY.new(const_vars[matrix[row][column]-1], var))
            end
        end
    end
    
    #row constraints
    for row in variable_matrix do
        vars = Variable[row.length].new
        for i in 0...row.length do
            vars[i] = row[i]
        end
        store.impose(Alldifferent.new(vars))
    end
    #column constraints
    for columnid in 0...variable_matrix[0].length do
        vars = Variable[variable_matrix.length].new    
        for rowid in 0...variable_matrix.length do
            vars[rowid] = variable_matrix[rowid][columnid]
        end
        store.impose(Alldifferent.new(vars))
    end

    #block constraints
    groups = [ [ nil, nil, nil],
               [ nil, nil, nil],
               [ nil, nil, nil]
             ]
    #init
    for i in 0...3 do
        for j in 0...3 do
            groups[i][j] = Variable[9].new
        end
    end
    
    for columnid in 0...variable_matrix[0].length do
        for rowid in 0...variable_matrix.length do
            grow = rowid / 3
            gcolumn = columnid / 3
            offset = 3 * (rowid % 3) + (columnid % 3)
            groups[grow][gcolumn][offset] = variable_matrix[rowid][columnid]
        end
        #
    end
    #impose
    for i in 0...3 do
        for j in 0...3 do
            store.impose(Alldifferent.new(groups[i][j]))
        end
    end

    
    label  = DepthFirstSearch.new()
    select = InputOrderSelect.new(store, const_vars + variable_matrix.flatten, IndomainMin.new)
    result = label.labeling(store, select)
    
    #puts variable_matrix[0][0].value, variable_matrix[0][0].value
    return variable_matrix[0][0].value*100 + variable_matrix[0][1].value * 10 + variable_matrix[0][2].value
end

k = 0

matrixes = LoadFromFile("sudoku.txt") { |matrix|
                                        k += SolveProblem(matrix)
                                        #print k
                                        #exit()
                                       }

puts "Sol = #{k}"
with open('matrix.txt', 'r') as fin:
    with open('matrix.js', 'w') as fout:
        print >> fout, "var matrix = ["

        for line in fin:
            line = line.strip()
            print >> fout, "\t[" + line + "],"
        print >> fout, "]"

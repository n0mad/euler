with open('matrix.txt', 'r') as fin:
    with open('matrix.h', 'w') as fout:
        print >> fout, "float matrix[][] = {"

        for line in fin:
            line = line.strip()
            print >> fout, "\t{" + line + "},"
        print >> fout, "}"

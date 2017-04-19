import sys
def ifEnglish(string):
    return ('a' in string.split())
triplets = [(x1,x2,x3) for x1 in xrange(97, 123) for x2 in xrange(97, 123) for x3 in xrange(97, 123)]

file = open(sys.argv[1], 'rb')
cipher = map(int, file.readline().split())
#cipher = map(lambda x: x^97, map(ord, 'a banana'))
file.close()


for triplet in triplets:
    decipher = []
    for i in xrange(len(cipher)):
        decipher.append(cipher[i] ^ triplet[i % 3])
    plaintext = map(chr, decipher)
    plaintext = ''.join(plaintext)
    if ifEnglish(plaintext):
        print plaintext
        print sum(decipher)
        print ''.join(map(chr, triplet))
    
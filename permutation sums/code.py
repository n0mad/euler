def nextLexPermutation(list):
    min_max = argmax(list)
    for i in xrange(len(list) - 1, 0, -1):
        if list[i] < list[i + 1]:
            for j in xrange(i, len(list)):
                if list[min_max] > list[j] > list[i]:
                    min_max = j
            
            list[i], list[j] = list[j], list[i]
        
            r = len(list)
            s = i + 1
            
            while (r > s):
                list[r],list[s] = list[s], list[r]
                r -= 1
                s += 1
                
                
lst = [1,2,3,4,5,6,7]
print lst
nextLexPermutation(lst)
print lst
nextLexPermutation(lst)
print lst
nextLexPermutation(lst)
print lst
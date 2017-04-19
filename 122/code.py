def check(aset, steps, bound , target):
    if steps == bound:
        return -1
        
    for a in aset:
        for b in aset:
            new = a + b
            if new in aset:
                continue
            if new == target:
                print aset,new, steps + 1
                return steps + 1
            aset.add(new)
            t = check(aset, steps + 1, bound, target)
            if t > -1:
                return t
            aset.remove(new)
    return -1
        
print check(set([1]), 0, 25, 200)
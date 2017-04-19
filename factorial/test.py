c_11, c_12, c_21, c_22 = 1, 1, 1, 0
#k = 1
import sys
n = int(sys.argv[1])

def mul( a_11, a_12, a_21, a_22, b_11, b_12, b_21, b_22):
    return a_11 * b_11 + b_21 * a_12, 
while not n == 0:
    if n % 2 == 1 or n == 2:
        c_11_new = c_11 + c_12
        c_21_new = c_21 + c_22
        c_12_new = c_11
        c_22_new = c_21
        
        c_11, c_12, c_21, c_22 = c_11_new, c_12_new, c_21_new, c_22_new
        #k += 1
        n = n - 1
        
    else:
        c_11_new = c_11*c_11 + c_12*c_21
        c_21_new = c_21*c_11 + c_22*c_12
        c_12_new = c_12*c_11 + c_22 * c_12
        c_22_new = c_12*c_21 + c_22*c_22

        c_11, c_12, c_21, c_22 = c_11_new, c_12_new, c_21_new, c_22_new
        
        n = n / 2
print c_11 + c_12, c_12 + c_22
#print c_11, c_12, c_22
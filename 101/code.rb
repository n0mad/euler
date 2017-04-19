def function(n)
    #return n*n*n #
    return 1 + n *( -1 + n * (1 + n * (-1 + n* (1 + n * (-1 + n* ( 1 + n * (-1 + n * (1 + n * (-1 + n)))))))))
end

def n!(n)
    k = 1
    for i in 1..n do
        k = k * i
    end
    return k
end

def factorPoly(power, point)
    res = 1
    for i in 0...power do
        res = res * (point - i)
    end
    return res
end

def calcPoly(coefficients, point)
    res = 0
    for i in 0...coefficients.length do
        res += coefficients[i] * factorPoly(i, point)
    end
    return res
end


#test = [1,2, 1]
#puts "#{calcPoly(test, 5)}"


def generatePoly(arrayOfY)
    if arrayOfY == nil or arrayOfY.length == 0 or arrayOfY[0] == nil
        return
    end
    coefficients = [arrayOfY[0]*1.0]
    #value = arrayOfY[0]
    
    for i in 1...arrayOfY.length do
        coefficient = ( arrayOfY[i] - calcPoly(coefficients, i)) *1.0 / (n!(i))
        #puts "coeff #{i} is #{coefficient}"
        coefficients << coefficient
        #value += coefficient * factorPoly(i, point)
    end
    return coefficients #calcPoly(coefficients, point)
end

def tostr(poly)
    str = ""
    for x in poly do
        str << " " << x.to_s
    end
    return str
end

#puts generatePoly([0,1,8,27])
#puts n!(3)
#puts factorPoly(3,2)

x = [1,2,3,4,5, 6, 7, 8, 9, 10, 11]

y = x.collect() { |i| function(i) }

k = 0
for i in 0...x.length - 1 do
    puts i
    coeffs = generatePoly(y[0..i])
    puts "f(#{x[i+1]}) = #{y[i+1]}, it is approximated with #{tostr(coeffs)} as #{calcPoly(coeffs, x[i])}"
    k += calcPoly(coeffs, x[i])
    puts "!!!#{k}"
end


#for i in 1...x.length do
#i = 100
#puts "while approximation in #{i} is approx #{generatePoly([0,1,4], i)}"
#end
#=end


f_prev_prev, f_prev, f = 1, 2, 3
a, b, c = 1, 1, 1
Terminal = 10**6 - 1 #9

while 1 do
    if f + f_prev  > Terminal then
        break
    end
    puts "a = #{a} b = #{b} c = #{c} f_prev_prev = #{f_prev_prev} f_prev = #{f_prev}, f = #{f}"
    f_prev_prev, f_prev, f = f_prev, f, f + f_prev
    a, b, c = a + b, c, f_prev_prev - 1 + a + b
    
end
puts "a = #{a} b = #{b} c = #{c} f_prev_prev = #{f_prev_prev} f_prev = #{f_prev}, f = #{f}"
density = 1 + c / (f_prev_prev)

puts "result = #{a + b + c +  density * (Terminal - f)}"
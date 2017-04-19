
import re

iv = re.compile("IV")
ix = re.compile("IX")
xl = re.compile("XL")
xc = re.compile("XC")
cd = re.compile("CD")
cm = re.compile("CM")
i = re.compile("I" )
v = re.compile("V" )
x = re.compile("X" )
l = re.compile("L" )
c = re.compile("C" )
d = re.compile("D" )
m = re.compile("M" )

def RomanNumeralsToDecimal(roman_string):
    import re, string
    str = string.upper(roman_string)
    exp = ""
    if iv.search(str) != None:  str = iv.sub("+4",    str)
    if ix.search(str) != None:  str = ix.sub("+9",    str)
    if xl.search(str) != None:  str = xl.sub("+40",   str)
    if xc.search(str) != None:  str = xc.sub("+90",   str)
    if cd.search(str) != None:  str = cd.sub("+400",  str)
    if cm.search(str) != None:  str = cm.sub("+900",  str)
    if  i.search(str) != None:  str =  i.sub("+1",    str)
    if  v.search(str) != None:  str =  v.sub("+5",    str)
    if  x.search(str) != None:  str =  x.sub("+10",   str)
    if  l.search(str) != None:  str =  l.sub("+50",   str)
    if  c.search(str) != None:  str =  c.sub("+100",  str)
    if  d.search(str) != None:  str =  d.sub("+500",  str)
    if  m.search(str) != None:  str =  m.sub("+1000", str)
    exec "num = " + str
    return num
    

def DecimalToRomanNumerals(base10_integer):
    '''Translated from a public domain C routine by Jim Walsh in the
    Snippets collection.
    '''
    roman = ""
    n, base10_integer = divmod(base10_integer, 1000)
    roman = "M"*n
    if base10_integer >= 900:
        roman = roman + "CM"
        base10_integer = base10_integer - 900
    while base10_integer >= 500:
        roman = roman + "D"
        base10_integer = base10_integer - 500
    if base10_integer >= 400:
        roman = roman + "CD"
        base10_integer = base10_integer - 400
    while base10_integer >= 100:
        roman = roman + "C"
        base10_integer = base10_integer - 100
    if base10_integer >= 90:
        roman = roman + "XC"
        base10_integer = base10_integer - 90
    while base10_integer >= 50:
        roman = roman + "L"
        base10_integer = base10_integer - 50
    if base10_integer >= 40:
        roman = roman + "XL"
        base10_integer = base10_integer - 40
    while base10_integer >= 10:
        roman = roman + "X"
        base10_integer = base10_integer - 10
    if base10_integer >= 9:
        roman = roman + "IX"
        base10_integer = base10_integer - 9
    while base10_integer >= 5:
        roman = roman + "V"
        base10_integer = base10_integer - 5
    if base10_integer >= 4:
        roman = roman + "IV"
        base10_integer = base10_integer - 4
    while base10_integer > 0:
        roman = roman + "I"
        base10_integer = base10_integer - 1
    return roman
    
    
f = open("roman.txt", 'r')
old_size, new_size = 0, 0 
for line in f:
    old_size += len(line.strip())
    integer = RomanNumeralsToDecimal(line.strip())
    new_size += len( DecimalToRomanNumerals(integer ))
    
f.close()

print old_size - new_size

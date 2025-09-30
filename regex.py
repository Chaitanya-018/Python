#REGEX is a one of the data type


import re   #to use regex we have to use module re

# regex=r"hello"
# ip="hello world"
# x=re.match(regex,ip)
# print(x)

#match

regex=r"hello"
ip="hello world"
op=re.match(regex,ip)
print(op)

regex=r"hello"   #output will be none
ip="hi hello world"
op=re.match(regex,ip)
print(op)

#search

regex=r"world"
ip="hello world"
op=re.search(regex,ip) # It will saerch anywhere
print(op)

#findall

regex=r"hello"   #It will check all the matchs and gives them all in the list
ip="hello hi hello hii hello"
op=re.findall(regex,ip)
print(op)

#----------------------------------------------------------------------------
#starts with character and ends with the character

regex=r"a.b"
#
# op=re.match(regex,"a/b")
# op=re.match(regex,"a+b")
# op=re.match(regex,"a8b")
# op=re.match(regex,"a:b")
op=re.match(regex,"a*b")
print(op)


#^ (cap) starts with

regex=r"^abc"
op=re.match(regex,"abcChaitu")  #valid input
if(op):
    print("valid input")
else:
    print("invalid input")


regex=r"xyz"
op=re.match(regex,"abcHello") #invalid
if(op):
    print("valid")
else:
    print("invalid")

#------------------------------------------------------------------
#$ for ending
regex=r"xyz$"
op=re.search(regex,"ABCxyz")
if(op):
    print("valid")
else:
    print("invalid")

regex=r"abc$"
op=re.search(regex,"ABCxyz")   #invalid
if(op):
    print("valid")
else:
    print("invalid")


#-----------------------------------------------------------------------------
#/d  > it will check for all the digits from 0 to 9

regex = r"^hdfc\d$"   # hdfc followed by exactly 1 digit
op = re.search(regex,"hdfc1")
if op:
    print("valid")
else:
    print("invalid")

regex = r"^hdfc\d+$"   # hdfc followed by exactly 1 digit
op = re.search(regex,"hdfc123")
if op:
    print("valid")
else:
    print("invalid")

#combination of upper case ,lower case and number
regex=r"[a-z A-Z 3-7]"
op=re.search(regex,"gR5")
if(op):
    print("valid")
else:
    print("invalid")


regex=r"(a-f)"
op=re.search(regex,"hi a-f hii")
if(op):
    print("valid")
else:
    print("invalid")


#{} -to define length
#{5} should have exactly length of 5
#{5,} min length is 5
#{5,10} min 5 ,max is 10

#pan card validation

regex=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
ip="OKLHJ3028Q"
op=re.search(regex,ip)
if(op):
    print("valid")
else:
    print("invalid")

#valid indian phone number

regex=r"^[6-9]{1}[0-9]{9}$"
ip="8008331645"
op=re.search(regex,ip)
if(op):
    print("valid")
else:
    print("invalid")

regex=r"^(\+91)\s[6-9]{1}[0-9]{9}$"
ip="+91 8008331645"
op=re.search(regex,ip)
if(op):
    print("valid")
else:
    print("invalid")

#pin number
x=r"^[1-9]{1}[0-9]{5}$"
ip="524005"
op=re.search(x,ip)
if(op):
    print("valid")
else:
    print("invalid")



# YYYY-MM-DD
regex = r"^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"

tests = ["2025-09-26", "1999-02-05", "2025-12-01", "2025-09-32"]

for ip in tests:
    if re.search(regex, ip):
        print(ip, "valid")
    else:
        print(ip, "invalid")





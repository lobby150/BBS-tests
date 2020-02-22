from pip._vendor.msgpack.fallback import xrange
import sys
from itertools import groupby

p = 11699
q = 7219
M = p * q


def gcd(a, b):
    while a != b:
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a


def seed(s):
    if s == 0:
        print("Seed must'nt be zero")
    elif s == 1:
        print("Seed must'nt be one")
    elif gcd(s, M) != 1:
        print("Seed must be coprime to M")
    else:
        print("Seed is coprime to M")
        return s


def getRandNum(a, bits):

    while bits:

        a = (a ** 2) % M
        bits -= 1
        if a%2 ==0:

            yield str(0)
        else:
            yield str(1)



def get_random(seed):
    return ''.join(getRandNum(seed, 20000))


x = int(input("Podaj wartosc seeda\n"))

seed(x)

print("\n")

print(get_random(x))

txt = get_random(x)

print("Test pojedynczych bitow: ilosc jedynek w ciagu, powinno ich byc w zakresie 9654;10346: \n")

a = 0
for c in txt:
    if c == '1':
        a = a + 1

print("Ilosc jedynek: " + str(a))

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
thirteen = 0
fourteen = 0
fifteen = 0
for i in range(0, len(txt), 4):
    txt4 = txt[i:i + 4]

    if txt4 == "0000":
        zero = zero + 1
    elif txt4 == "0001":
        one = one + 1
    elif txt4 == "0010":
        two = two + 1
    elif txt4 == "0011":
        three = three + 1
    elif txt4 == "0100":
        four = four + 1
    elif txt4 == "0101":
        five = five + 1
    elif txt4 == "0110":
        six = six + 1
    elif txt4 == "0111":
        seven = seven + 1
    elif txt4 == "1000":
        eight = eight + 1
    elif txt4 == "1001":
        nine = nine + 1
    elif txt4 == "1010":
        ten = ten + 1
    elif txt4 == "1011":
        eleven = eleven + 1
    elif txt4 == "1100":
        twelve = twelve + 1
    elif txt4 == "1101":
        thirteen = thirteen + 1
    elif txt4 == "1110":
        fourteen = fourteen + 1
    elif txt4 == "1111":
        fifteen = fifteen + 1

print("0: " + str(zero))
print("1: " + str(one))
print("2: " + str(two))
print("3: " + str(three))
print("4: " + str(four))
print("5: " + str(five))
print("6: " + str(six))
print("7: " + str(seven))
print("8: " + str(eight))
print("9: " + str(nine))
print("10: " + str(ten))
print("11: " + str(eleven))
print("12: " + str(twelve))
print("13: " + str(thirteen))
print("14: " + str(fourteen))
print("15: " + str(fifteen))
print("\n")

wynik = 0.0

wynik = ((one * one) + (zero*zero) +  (two * two) + (three * three) + (four * four) + (five * five) + (six * six) + (seven * seven) + (
            eight * eight) + (nine * nine) + (ten * ten) + (eleven * eleven) + (twelve * twelve) + (
                     thirteen * thirteen) + (fourteen * fourteen) + (fifteen * fifteen))
print(wynik)
result = 0.0

result = (((16 / 5000) * wynik) - 5000)
result1 = round(result,2)
print("Wynik testu pokerowego: " + str(result1))
if result > 2.16 and result < 46.17:
    print("Test pokerowy powiodl sie")
else:
    print("Test pokerowy nie powiodl sie")

jeden = 0
dwa = 0
trzy = 0
cztery = 0
piec = 0
szesc = 0
max = 0
for k, g in groupby(txt):
    my_list = list(g)

    if len(my_list) == 1 and my_list == ['0']:
        jeden = jeden + 1
    elif len(my_list) == 2 and my_list == ['0', '0']:
        dwa = dwa + 1
    elif len(my_list) == 3 and my_list == ['0', '0', '0']:
        trzy = trzy + 1
    elif len(my_list) == 4 and my_list == ['0', '0', '0','0']:
        cztery = cztery + 1
    elif len(my_list) == 5 and my_list == ['0', '0','0','0','0']:
        piec = piec + 1
    elif len(my_list) >= 6 and my_list.__contains__(str(0)):
        szesc = szesc + 1
    elif len(my_list) > 26:
        max =+ 1
print("Test serii: \n")
print("Ciagi 1-elementowe: " + str(jeden))
print("Ciagi 2-elementowe: " + str(dwa))
print("Ciagi 3-elementowe: " + str(trzy))
print("Ciagi 4-elementowe: " + str(cztery))
print("Ciagi 5-elementowe: " + str(piec))
print("Ciagi 6-elementowe i więcej: " + str(szesc))
#seed 6451

if max>0:
    print("Test dlugiej serii nie powiodl sie\n")
else:
    print("Test dlugiej serii sie powiodl\n")


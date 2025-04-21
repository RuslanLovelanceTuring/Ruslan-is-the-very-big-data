Sprint_1a task

#1) 

num = 123
char_num = str(num)
print(char_num, type(char_num))

#2) 

price = 19.99
int_price = int(price)
print(int_price)

#3) 

val = "500"
num_val = int(val)
print(num_val / 2)

#4) 

a = 8
b = 12
print(a < b)
print(a == b)


#5) 
x, y, z = 5, 10, 15
print((x < y) and (y < z))

#6) 

print(25 // 4)  # tam bölmə
print(25 % 4)   # qalıq
print(25 / 4)   # adi bölmə

#7) 

print(3 ** 4)

#8)

qiymet = 75.5
int_qiymet = int(qiymet)
print(int_qiymet, type(int_qiymet))

#9)

n = 20
print((n > 10) or (n < 5))
print((n > 15) and (n < 25))

#10) 

val = "42.8"
float_val = float(val)
print(float_val, type(float_val))
int_val = int(float_val)
print(int_val, type(int_val))



Sprint_1b task


#1) 

s = "Programming"
print(len(s), s[0])


#2) 

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#3) 

text = "Python"
print(text[-1])

#4) 

s = "Artificial"
print(s[:3])

#5) 

word = "Code"
print(word[::-1])

#6) 

s = "abcdefgh"
print(s[::2])

#7) 

text = "data"
print(text.upper(), text.lower())

#8) 

s = "Python-R-Java"
print(s.split("-"))

#9) 

ad = "Ayxan"
yas = 25
print(f"{ad} {yas} yaşındadır")

#10) 

s = "salam-muallim"
print(s.replace("-", " "))


 Sprint_2a_task


#1) 

reqemler = [5, 10, 15, 20]

#2) 

print("Uzunluq:", len(reqemler))

#3)

reqemler.append(25)
print("yeni reqem əlavə olundu:", reqemler)

#4)

reqemler.insert(2, 12)
print("2-ci indeksə 12 əlavə olundu:", reqemler)


#5) 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis_list = list1 + list2
print("Birləşmiş list:", birlesmis_list)

#6) 

print("2-ci və 3-cü elementlər:", reqemler[2:4])

#7) 

reqemler[0] = 50
print("İlk element 50 ilə əvəz olundu:", reqemler)

#8) 

print("19 listdə var?", 19 in reqemler)

#9) 

herfler = ["a", "b", "a", "c"]
print("'a' neçə dəfə var:", herfler.count("a"))

#10) 

simvollar = ["x", "y", "x", "z"]
while "x" in simvollar:
    simvollar.remove("x")
print("'x' silindikdən sonra:", simvollar)

#11) 

nums = [7, 2, 9, 1]
nums.sort(reverse=True)
print("Azalan sırayla:", nums)

#12) 

boyuk_10 = [x for x in reqemler if x > 10]
print("10-dan böyük elementlər:", boyuk_10)


Sprint_2b_task

import pandas as pd

#1) 

s1 = pd.Series([10, 20, 30, 40])

#2)

s1.index = ['w', 'x', 'y', 'z']
print("s1:\n", s1)

#3) 
    R: list(p = 5, q = 10, r = 15) listindən v2 adlı named vektor yaradın

data_dict = {'p': 5, 'q': 10, 'r': 15}
s2 = pd.Series(data_dict)
print("s2:\n", s2)


#4) 

print("s2['q']:", s2['q'])


#5) 

print("25-dən böyük elementlər:\n", s1[s1 > 25])


#6)

print("20-dən böyük elementləri 10-a böl:\n", s1[s1 > 20] / 10)

#7) 

df1 = pd.DataFrame([(1, 2), (3, 4)])

#8) 

df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
print("df1:\n", df1)


#9) 

df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("df2:\n", df2)

#10) 

print("A sütunu 1-dən böyük olan sətirlər:\n", df2[df2['A'] > 1])
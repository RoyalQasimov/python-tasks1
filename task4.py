boy = float(input("boy:"))
kutle = float(input("kutle:"))

bki = kutle/ boy * boy

if bki < 18.5:
    a = "zeif"
elif 18.5 <= bki < 25:
    a = "normal"
elif 25 <= bki < 30:
    a = "kilolu"
else :
    a = "obez"
print(a)
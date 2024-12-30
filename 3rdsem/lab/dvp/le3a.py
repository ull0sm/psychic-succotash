string = input("enter the STRING:")

upper = 0
lower = 0
digits = 0
special = 0
words = len(string.split())

for i in string:
    if i != " ":
        if i.isupper():
            upper +=1
        elif i.islower():
            lower +=1
        elif i.isdigit():
            digits +=1
        else:
            special +=1
        

print(f"words: {words}")
print(f"Upper: {upper}")
print(f"Lower: {lower}")
print(f"Digits: {digits}")
print(f"special: {special}")

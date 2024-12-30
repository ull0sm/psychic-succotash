num = (input("enter the number:"))

if num != num[::-1]:
    print("it is not a palindrome")
else:
    print("it is a palindrome")
    
digits = {}

for i in num:
    if i in digits:
        digits[i] +=1
    else:
        digits[i] = 1

print(digits)
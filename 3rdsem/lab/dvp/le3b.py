s1 = input("enter the first string:").strip()
s2 = input("enter the second string:").strip()

sim = 0

if len(s1)>len(s2):
    shorter_string = s2
    longer_string = s1
else:
    shorter_string = s1
    longer_string = s2
    
for i in range(len(shorter_string)):
    if(shorter_string[i]==longer_string[i]):
        sim +=1
    
ans = (sim/len(shorter_string))*100

print(f"the answer is: {ans:.2f}%")
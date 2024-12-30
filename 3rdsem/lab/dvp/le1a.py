a = [0,0,0]
try:
    for i in range(3):
        print(f"enter the {i+1}th:")
        a[i] = int(input())
except:
    print("invalid entry:")

low = min(a);

print(f"\nthe lowest of all is : {low}")
print(f"the average of the best two is : {(sum(a)-low)/2}\n")
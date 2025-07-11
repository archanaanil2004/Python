c=set()
A={"a","e","i","o","u"}
B=str(input("Enter a sentence:"))
for i in B:
    if i in A:
        c.add(i)
print("existing vowels are:",c)
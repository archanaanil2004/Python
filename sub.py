subjects = (input("Enter  the subjects (comma-separated): ")).split(",")
studied = (input("Enter subjects you already studied (comma-separated): ")).split(",")

no_studied=[]
for sub in subjects:
    if sub not in studied:
        no_studied.append(sub)
print("\n subjects left to study:")
for sub in no_studied:
    print("-",sub)
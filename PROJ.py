startYear = int(input("enter the start date: "))
endYear = int(input("enter the end date"))
S=[]
b=[]
for year in range(startYear, endYear):
    if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
        S.append(year)
    else:
        b.append(year)
print("leap years are : ",S)
print("non-leap years are:",b)
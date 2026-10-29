startYear=int(input("Enter the start year:"))
print("Enter the lastyear")
endYear=int(input("Enter the end year:"))
print("list of leap years:")
for year in range(startYear,endYear):
 if((year%4==0)and(year%100!=0))or(year%400==0):
  print(year)

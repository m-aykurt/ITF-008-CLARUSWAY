year = int(input("yil giriniz: "))

leap = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

if (leap == True):
    print(f"Yes, this {year} year is a leap year")
else:
    print(f"oh No, {year} is not leap year.")
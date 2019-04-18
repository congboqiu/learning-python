def is_leap(year):
    leap=False
    if year%4==0:
        leap=True
        if year%100==0 and year%400!=0:
            Leap=False
    return leap


print(bool(is_leap(2020)))

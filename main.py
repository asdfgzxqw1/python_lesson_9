print("Введи в меня деньги:")
a =float(input())

print("Сколько лет будешь хранить?:")
years = int(input())

def bank(a, years):
    i=0
    while i<years:
        a=a+a*0.1
        i=i+1
    return a


print(bank(a, years))



a=input("Unesi godinu:")
if a.isdigit():
    godina=int(a)
    if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
        print(godina, "je prijestupna godina.")
    else:
        print(godina, "nije prijestupna godina.")
z=input("Enter Your Name and Surname: ")
a = []
a.append(z)
liste = []
def abbrev_name(c):
    for i in c:
        b = str(i[0]).upper()
        liste.append(b)
for x in a:
    c = x.split()
    abbrev_name(c)
for i in liste:
   if i==liste[len(liste)-1]:
        print(i)
   else:
       print(i, end=".")

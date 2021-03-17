def sort_string(string):
   string = string.replace(" ", "")
   n = len(string)
   a = list()
   for i in range(n):
       a.append(string[i])
   a.sort()
   newstr=''.join(a)
   print(newstr)

print("Введите строку")
string = input()

sort_string(string)

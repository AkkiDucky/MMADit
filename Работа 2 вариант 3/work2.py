#2. Написать функцию, которая сортирует все буквы в строке по возрастанию и возвращает полу-чившуюся строку.
#Для преобразования строки в массив букв используйте встроенную функцию list.
#Для сортировки букв используйте функцию sorted. Для обратного преобразования строки в массив используйте конструкцию: ‘’.join(a), где a – это массив.

def sort_string(string):
   string = string.replace(" ", "")
   list(string)

   return ''.join(sorted(list(string)))

print("Введите строку")
string = input()

print(sort_string(string))

"""
Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""
inNumberList = input("Введите список чисел, разделённый пробелом\n")
xx = int(input("Введите искомое число: "))
lstlst = inNumberList.split()
res = ""
for i in range(len(lstlst)):
  if int(lstlst[i]) == xx:
    res += " "+ str(i)
if res == "":
  print("Отсутствует")
else:
  print (res)

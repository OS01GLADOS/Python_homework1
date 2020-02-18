"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера,
 у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
  У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
"""
inLine = input("Введите прямоугольную матрицу, \"end\" - для окончания строки \n ")
lst1 = inLine.split('end')
lstClear = inLine.split('end')

lst1.pop()
lstClear.pop()

print(lst1)

for i in range (len(lst1)):
  lst1[i]=lst1[i].split()

#задание
up =0
dwn=0
l =0
r =0

print(len(lstClear))
print(len(lstClear[0]))

for j in range (len(lstClear)-1):#перебор строк

  if len(lstClear)==1:
    up=0
    dwn=0
  elif j==0:
    up=(len(lstClear)-1)
    dwn=j+1
  elif j==(len(lstClear)-1):
    up = j-1
    dwn = 0
  else:
    up = j-1
    dwn = j+1

  for i in range (len(lstClear[0])-1):#перебор элементов
    if i!=0 or (i!= len(lstClear[i])-1):
      l = lstClear[j][i-1]
      r = lstClear[j][i+1]
    elif i==0:#1st
      l = lstClear[j][len(lstClear[i])]
      r = lstClear[j][i + 1]
    else:#last
      l = lstClear[j][i - 1]
      r = lstClear[j][0]
    up_i=lstClear[up][i]
    dwn_i=lstClear[dwn][i]
    lst1[i]=l+r+up_i+dwn_i
print(lst1)
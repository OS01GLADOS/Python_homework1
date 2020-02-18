"""выводит часть последовательности
 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
 (число повторяется столько раз, чему равно)
 """
a = int(input("Введите число: "))
start = 1
res =""
for i in range (a):
  for j in range (start):
    res= res +" "+str(start)
  start+=1
print (res)
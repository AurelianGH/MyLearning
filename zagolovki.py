# Преобразование заголовков из файла text.txt в формат Первая буква/количество символов

file = open("text.txt")
f = file.readlines() #file
l = len(f) #lenght
le= f[l-1] #last element

for i in f:
	
	if i != le:
		print(i[0] + str(len(i)-1))
	else:
		print(i[0] + str(len(i)))


file.close()
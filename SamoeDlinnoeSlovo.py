# Поиск самого длинного слова в тексте

txt = input("Ввод текста: ")
txt = txt.split()


lenght = 0

for i in txt:
	
	if len(i) > lenght:
		lenght = len(i)
		val = i
		
print('Самое длинное слово в тексте содержит ' + str(len(val)) + ' символов: ' + val)

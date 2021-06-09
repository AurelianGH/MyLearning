#Проверка слова на палиндром

while True:
	word = input('Введите слово для проверки на палиндром:\n(или выход - что бы выйти) ')
	if word == 'выход':
		break
	for i in range(len(word)):
		imir = word[(len(word) - 1) - i] #i зеркальное
		tst = word[i]
		if tst == imir:
			p = True
		else:
			p = False
			break
	if p:
		print('Это слово палиндром\n')
	else:
		print('Нет, это не палиндром\n')
print('\nПрограмма завершена')
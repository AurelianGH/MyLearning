# Поиск слова в тексте

text = input()
word = input()

def search (txt, wrd):
    notFind = True
    for i in txt.split():
    	if wrd == i:
    		print('Word found')
    		nf = False
    if notFind:
    	print('Word not found')
    		
    		

search(text, word)
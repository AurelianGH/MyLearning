#Расчет Индекса Массы Тела

#Underweight = меньше 18.5
#Normal = 18.5 - 24.9
#Overweight = 25 - 29.9
#Obesity = 30 и больше

mass = int(input())
height = float(input())

IMT = mass/(height**2)
IMT = IMT - (IMT % 0.1)
if IMT < 18.5 :
	print("Underweight")
elif IMT >= 18.5 and IMT <= 24.9:
	print("Normal")
elif IMT >= 25 and IMT <= 29.9:
	print("Overweight")
elif IMT >= 30 :
	print("Obesity")
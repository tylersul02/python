#convertkmmi.py trs
def print_menu():
	print('1. Kilometers to Miles')
	print('2. Miles to Kilometers')
	
def km_miles():
	km = float(input('Enter distance in kilometers: '))
	miles = km / 1.609
	
	print('Distance in miles: {0}'.format(miles))
	
def miles_km():
	miles = float(input('Enter distance in miles: '))
	km = miles * 1.609
	
	print('Distance in Kilometers:{0}'.format(km))
	
if __name__== '__main__':
	print_menu()
	choice = input('Which coversion would you like to do? 1 or 2?: ')
	if choice == '1':
		km_miles()
		
	if choice == '2':
		miles_km()

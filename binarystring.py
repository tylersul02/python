# binarystring.py trs
def bincon(decimal):
	print("BINARY\n")
	print(decimal)
	binstr=""
	for i in range(8):
		bin = decimal % 2
		binstr = binstr + str(bin)
		decimal = decimal // 2
		print (bin)
	print(binstr)

def main():
	print("input a -1 to exit the loop")
	print("input an integer < 256 and > -1")
	done = 0;
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
main()

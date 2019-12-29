import qrcode, random

FLAG = "X-MAS{Th@t's_4_w31rD_fUnCt10n!!!_8082838205}"

qr = qrcode.QRCode (
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    border = 1,
)

qr.add_data (FLAG)
qr.make (fit = True)
arr = qr.get_matrix ()

pool = []

for i in range (len (arr)):
	for k in range (len (arr[0])):
		pool.append ((i, k))

random.shuffle (pool)
nbGuesses = len (pool)

intro = """Welcome to my guessing service!
Can you guess all {} values?\n\n""".format (nbGuesses)
print (intro)

correct = 0

for round in range (nbGuesses):
    x = pool[round][0]
    y = pool[round][1]
    
    guess = input ("f({}, {})=".format (x, y))
    
    if (int (guess) == int (arr[x][y])):
        print ("Good!\n")
        correct += 1
    else:
        print ("Pretty close, but wrong!\n")

if correct == nbGuesses:
    print ("Great! You did it! Now what?\n")
else:
    print ("Maybe another time :(\n")

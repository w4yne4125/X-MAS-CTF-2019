from PIL import Image, ImageColor

im = Image.new('1', (31,31)) # create the Image of size 1 pixel 
# im.putpixel((0,0), ImageColor.getcolor('black', '1')) # or whatever color you wish

# im.save('result.png') # or any image format

f = open("text.txt","r")
cnt = 0
lineNum = 0
for lines in f:
	if lines[0] == "1":
		im.putpixel((lineNum,cnt), ImageColor.getcolor('black', '1'))
		print(" ", end = "")
	else:
		im.putpixel((lineNum,cnt), ImageColor.getcolor('white', '1'))
		print("0", end="")
	cnt += 1
	if cnt == 31:
		print("")
		cnt = 0
		lineNum += 1

im.save('result.png')
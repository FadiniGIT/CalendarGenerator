from PIL import Image, ImageDraw, ImageFont


font = ImageFont.truetype("/Library/Fonts/Arial Unicode.ttf", 175)

print("What day of the week is the 1st of the Month?")
print("(1) Monday")
print("(2) Tuesday")
print("(3) Wednesday")
print("(4) Thursday")
print("(5) Friday")
print("(6) Saturday")
print("(7) Sunday")
day = int(input("Pick a number: "))
dayNum_c = day - 1
name_ctr = dayNum_c
print("Generating Calendar...")

def generateCalendars(pagenum):
	global name_ctr

	img = Image.new('RGB', (3300, 2550), color = 'white')
	draw = ImageDraw.Draw(img)

	draw.line((300,0,300,2550), fill=0, width=20)
	draw.line((600,0,600,2550), fill=0, width=20)

	scale_down_line_y = 320
	for i in range(1,8):
		draw.line((0,scale_down_line_y,3300,scale_down_line_y), fill=0, width=20)
		scale_down_line_y = scale_down_line_y + 320

	scale_down_text_y = 50

	if pagenum == 1:
		startnum = 1
		endnum = 9

	elif pagenum == 2:
		startnum = 9
		endnum = 17

	elif pagenum == 3:
		startnum = 17
		endnum = 25
	
	elif pagenum == 4:
		startnum = 25
		endnum = 32

	
	names = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
	
	for i in range(startnum,endnum):

		if i <10:
			draw.text((90,scale_down_text_y), str(i), fill=0, font=font, stroke_width=10)
			draw.text((320,scale_down_text_y), str(names[name_ctr]), fill=0, font=font, stroke_width=10)
			name_ctr = name_ctr + 1
			if name_ctr == 7:
				name_ctr = 0
			scale_down_text_y = scale_down_text_y + 320


		else:
			draw.text((40,scale_down_text_y), str(i), fill=0, font=font, stroke_width=10)
			draw.text((320,scale_down_text_y), str(names[name_ctr]), fill=0, font=font, stroke_width=10)
			name_ctr = name_ctr + 1
			if name_ctr == 7:
				name_ctr = 0
			scale_down_text_y = scale_down_text_y + 320

	img.save(f'calendar{pagenum}.png')

for i in range(1,5):
	generateCalendars(i)


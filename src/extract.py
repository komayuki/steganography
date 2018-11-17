from PIL import Image
import os
import sys
import re

def extract(src):
	img = Image.open(src)
	rgb_img = img.convert("RGB")
	img_size = rgb_img.size

	arr = []
	index = 0
	binary = ''
	for x in range(img_size[0]):
		for y in range(img_size[1]):
			r, g, b = img.getpixel((x, y))
			rgb = [r, g, b]
			for c in rgb:
				if index == 7:
					char = chr(int(binary, 2))
					m = re.match(r"[a-zA-Z0-9]", char)
					if len(char) == 1 and m:
						arr.append(char)
					binary = ''
					index = 0
				binary += bin(c)[len(bin(c))-1]
				index = index + 1

	print("".join(arr))

if __name__ == '__main__':
	args = sys.argv
	extract(args[1])

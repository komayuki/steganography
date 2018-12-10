from PIL import Image
import os
import sys
import re

dir = os.path.dirname(__file__)
img_path = os.path.join(dir, "img/img.png")

def hidden_keys(text):
	codepoints = [hex(ord(t))[2:] for t in text]
	keys = []
	for h1 in codepoints:
		binary = bin(int(str(h1), 16))[2:].zfill(7)
		for b1 in list(str(binary)):
			keys.append(b1)

	return keys


def generate(text):
	keys = hidden_keys(text)
	im = Image.open(img_path)
	rgb_im = im.convert("RGB")
	im_size = rgb_im.size

	im2 = Image.new("RGB", im_size)

	i_1 = 0
	for x in range(im_size[0]):
		for y in range(im_size[1]):
			r, g, b = rgb_im.getpixel((x, y))

			rgb = [r, g, b]
			for i_2 in range(len(rgb)):
				c = rgb[i_2]
				if i_1 < len(keys):
					c_b = bin(c)[:-1] + str(keys[i_1])
					rgb[i_2] = (int(c_b, 2))
					i_1 = i_1 + 1

				if i_1 == len(keys):
					i_1 = 0

			r = rgb[0]
			g = rgb[1]
			b = rgb[2]

			im2.putpixel((x,y),(r,g,b,0))

	im2.save(os.path.join(dir, "img/output.png"))

if __name__ == '__main__':
	generate("  great!! pass: hogehogeman!  ")
